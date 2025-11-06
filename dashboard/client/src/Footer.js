import React from 'react';
import { Box, Typography, Link } from '@mui/material';

function Footer() {
  return (
    <Box 
      component="footer" 
      sx={{
        p: 2, 
        mt: 'auto', 
        backgroundColor: 'primary.dark', 
        color: 'white', 
        textAlign: 'center'
      }}
    >
      <Typography variant="body2">
        Desenvolvido por Pedro Henrique Sauthier
      </Typography>
    </Box>
  );
}

export default Footer;
