import React from 'react';
import { Modal, Box, Typography, IconButton, Button } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import OpenInNewIcon from '@mui/icons-material/OpenInNew';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: '85vw',
  height: '90vh',
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 0,
  display: 'flex',
  flexDirection: 'column',
};

function FileModal({ open, handleClose, filePath, fileContent }) {
  if (!filePath) return null;

  const isHtml = filePath.endsWith('.html');
  const isImage = filePath.match(/\.(png|jpg|jpeg|gif)$/i);

  let content;
  if (isHtml) {
    content = <iframe srcDoc={fileContent} style={{ width: '100%', height: '100%', border: 'none' }} title={filePath}></iframe>;
  } else if (isImage) {
    content = <img src={fileContent} alt={filePath} style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }} />;
  } else {
    content = <pre style={{ whiteSpace: 'pre-wrap', wordWrap: 'break-word', padding: '16px' }}>{fileContent}</pre>;
  }

  return (
    <Modal open={open} onClose={handleClose}>
      <Box sx={style}>
        <Box 
          sx={{
            p: 2,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            borderBottom: '1px solid #ddd',
            backgroundColor: '#f5f5f5'
          }}
        >
          <Typography sx={{ fontWeight: 'bold' }}>{filePath}</Typography>
          <Box sx={{ display: 'flex', alignItems: 'center' }}>
            {(isHtml || isImage) && (
              <Button
                variant="contained"
                color="primary"
                size="large"
                startIcon={<OpenInNewIcon />}
                href={`http://localhost:5000/${filePath}`}
                target="_blank"
                rel="noopener noreferrer"
                sx={{ mr: 2, whiteSpace: 'nowrap' }}
              >
                Abrir em Nova Aba
              </Button>
            )}
            <IconButton onClick={handleClose}>
              <CloseIcon />
            </IconButton>
          </Box>
        </Box>
        <Box sx={{ 
          flexGrow: 1, 
          overflow: 'auto', 
          p: 2, 
          display: 'flex', 
          justifyContent: 'center', 
          alignItems: 'center' 
        }}>
          {content}
        </Box>
      </Box>
    </Modal>
  );
}

export default FileModal;
