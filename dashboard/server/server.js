const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// Serve artifact folders statically for direct access
const artifactsRoot = path.join(__dirname, '..', '..');
app.use('/reports', express.static(path.join(artifactsRoot, 'reports')));
app.use('/logs', express.static(path.join(artifactsRoot, 'logs')));
app.use('/screenshots', express.static(path.join(artifactsRoot, 'screenshots')));

// Define the root directory for your Playwright project
const PROJECT_ROOT = path.join(__dirname, '..', '..'); // Go up two levels from server.js

// Helper function to recursively read directory structure
function readDirectory(dirPath, relativePath = '') {
    const entries = fs.readdirSync(dirPath, { withFileTypes: true });
    const structure = [];

    for (const entry of entries) {
        const fullPath = path.join(dirPath, entry.name);
        const currentRelativePath = path.join(relativePath, entry.name).replace(/\\/g, '/');

        // Exclude node_modules, .git, and other non-relevant directories/files
        if (entry.isDirectory() && (entry.name === 'node_modules' || entry.name === '.git' || entry.name === 'playVenv' || entry.name === '__pycache__' || entry.name === '.pytest_cache' || entry.name === '.vscode' || entry.name === 'dashboard')) {
            continue;
        }
        if (entry.isFile() && (entry.name.startsWith('.') || entry.name.endsWith('.pyc') || entry.name.endsWith('.log') || entry.name.endsWith('.json') || entry.name.endsWith('.txt') || entry.name.endsWith('.md') || entry.name.endsWith('.ini') || entry.name.endsWith('.example')) ){
            continue;
        }

        if (entry.isDirectory()) {
            structure.push({
                name: entry.name,
                path: currentRelativePath,
                type: 'directory',
                children: readDirectory(fullPath, currentRelativePath)
            });
        } else {
            structure.push({
                name: entry.name,
                path: currentRelativePath,
                type: 'file'
            });
        }
    }
    return structure;
}

// API endpoint to get file structure
app.get('/api/files', (req, res) => {
    try {
        const reportsPath = path.join(PROJECT_ROOT, 'reports');
        const logsPath = path.join(PROJECT_ROOT, 'logs');
        const screenshotsPath = path.join(PROJECT_ROOT, 'screenshots');

        const structure = [
            {
                name: 'reports',
                path: 'reports',
                type: 'directory',
                children: fs.existsSync(reportsPath) ? readDirectory(reportsPath, 'reports') : []
            },
            {
                name: 'logs',
                path: 'logs',
                type: 'directory',
                children: fs.existsSync(logsPath) ? readDirectory(logsPath, 'logs') : []
            },
            {
                name: 'screenshots',
                path: 'screenshots',
                type: 'directory',
                children: fs.existsSync(screenshotsPath) ? readDirectory(screenshotsPath, 'screenshots') : []
            }
        ];
        res.json(structure);
    } catch (error) {
        console.error('Error reading file structure:', error);
        res.status(500).json({ error: 'Failed to read file structure' });
    }
});

// API endpoint to get file content
app.get('/api/file-content', (req, res) => {
    const filePath = req.query.path;
    if (!filePath) {
        return res.status(400).json({ error: 'File path is required' });
    }

    const absolutePath = path.join(PROJECT_ROOT, filePath);

    // Security check: ensure file is within the project root
    if (!absolutePath.startsWith(PROJECT_ROOT)) {
        return res.status(403).json({ error: 'Access denied' });
    }

    try {
        const fileExtension = path.extname(absolutePath).toLowerCase();
        if (fileExtension === '.html') {
            res.setHeader('Content-Type', 'text/html');
            fs.createReadStream(absolutePath).pipe(res);
        } else if (fileExtension === '.png' || fileExtension === '.jpg' || fileExtension === '.jpeg' || fileExtension === '.gif') {
            res.setHeader('Content-Type', `image/${fileExtension.substring(1)}`);
            fs.createReadStream(absolutePath).pipe(res);
        } else {
            // For other file types (e.g., .log), send as plain text
            res.setHeader('Content-Type', 'text/plain');
            fs.createReadStream(absolutePath).pipe(res);
        }
    } catch (error) {
        console.error(`Error reading file ${absolutePath}:`, error);
        res.status(500).json({ error: 'Failed to read file content' });
    }
});

// Serve static React files in production
if (process.env.NODE_ENV === 'production') {
    app.use(express.static(path.join(__dirname, '..', 'client', 'build')));

    app.get('*', (req, res) => {
        res.sendFile(path.join(__dirname, '..', 'client', 'build', 'index.html'));
    });
}

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
