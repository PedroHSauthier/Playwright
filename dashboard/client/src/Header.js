import React from 'react';
import { AppBar, Toolbar, Typography } from '@mui/material';

function Header() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Certa - Painel de Artefatos de Teste
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
