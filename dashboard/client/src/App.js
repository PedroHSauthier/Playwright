import React, { useState, useEffect } from 'react';
import { CssBaseline, ThemeProvider, Box, Typography } from '@mui/material';
import theme from './theme';
import Header from './Header';
import Footer from './Footer';
import FileTree from './FileTree';
import FileModal from './FileModal';

function App() {
  const [fileStructure, setFileStructure] = useState([]);
  const [selectedFile, setSelectedFile] = useState({ path: null, content: null });
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchFileStructure = () => {
    fetch('/api/files')
      .then(response => response.json())
      .then(data => setFileStructure(data))
      .catch(error => console.error('Error fetching file structure:', error));
  };

  useEffect(() => {
    fetchFileStructure(); // Fetch immediately on mount

    const intervalId = setInterval(fetchFileStructure, 5000); // Poll every 5 seconds

    return () => clearInterval(intervalId); // Cleanup on unmount
  }, []);

  const handleFileSelect = (filePath) => {
    fetch(`/api/file-content?path=${filePath}`)
      .then(response => {
        const contentType = response.headers.get('Content-Type');
        if (contentType && contentType.includes('image')) {
          return response.blob().then(blob => URL.createObjectURL(blob));
        } else {
          return response.text();
        }
      })
      .then(content => {
        setSelectedFile({ path: filePath, content: content });
        setIsModalOpen(true);
      })
      .catch(error => console.error('Error fetching file content:', error));
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedFile({ path: null, content: null });
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ display: 'flex', flexDirection: 'column', height: '100vh' }}>
        <Header />
        <Box sx={{ flexGrow: 1, overflowY: 'auto', p: 3 }}>
          <Typography variant="h5" gutterBottom>Navegador de Artefatos</Typography>
          <FileTree fileStructure={fileStructure} onFileSelect={handleFileSelect} />
        </Box>
        <Footer />
        <FileModal 
          open={isModalOpen} 
          handleClose={handleCloseModal} 
          filePath={selectedFile.path} 
          fileContent={selectedFile.content} 
        />
      </Box>
    </ThemeProvider>
  );
}

export default App;
