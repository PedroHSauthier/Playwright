import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

function FileViewer({ filePath, fileContent }) {
  if (!filePath) {
    return (
      <Box sx={{ p: 3, textAlign: 'center', color: 'grey.600' }}>
        <Typography variant="h6">Selecione um arquivo para visualizar</Typography>
      </Box>
    );
  }

  let content;
  if (filePath.endsWith('.html')) {
    content = <iframe srcDoc={fileContent} style={{ width: '100%', height: '100%', border: 'none' }} title={filePath}></iframe>;
  } else if (filePath.match(/\.(png|jpg|jpeg|gif)$/i)) {
    content = <img src={fileContent} alt={filePath} style={{ maxWidth: '100%', height: 'auto' }} />;
  } else {
    content = <pre style={{ whiteSpace: 'pre-wrap', wordWrap: 'break-word' }}>{fileContent}</pre>;
  }

  return (
    <Paper elevation={2} sx={{ height: '100%', overflow: 'auto' }}>
      <Box sx={{ p: 2, borderBottom: '1px solid #ddd' }}>
        <Typography variant="body2" sx={{ fontWeight: 'bold' }}>{filePath}</Typography>
      </Box>
      <Box sx={{ p: 2, height: 'calc(100% - 60px)', overflowY: 'auto' }}>
        {content}
      </Box>
    </Paper>
  );
}

export default FileViewer;
