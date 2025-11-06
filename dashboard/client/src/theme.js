import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2', // Blue
      dark: '#0d47a1', // Dark Blue
    },
    secondary: {
      main: '#ffffff', // White
    },
    error: {
      main: '#d32f2f', // Red
    },
    background: {
      default: '#ffffff', // White
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
  },
});

export default theme;
