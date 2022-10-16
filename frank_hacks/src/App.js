import * as React from 'react';
import Avatar from '@mui/material/Avatar';
//import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import SurfingIcon from '@mui/icons-material/Surfing';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Search from './search';

const theme = createTheme();

export default function Locate() {
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      text: data.get('text')
    });
  };

  return (
    <ThemeProvider theme={theme}>
      <Grid container component="main" sx={{ height: '100vh' }}>
        <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={7}
          sx={{
            backgroundImage: 'url(https://preview.redd.it/so6zsvih25u91.jpg?width=960&crop=smart&auto=webp&s=49b36ef972f741b9cb09e58687c35a6cba00e3bf)',
            backgroundRepeat: 'no-repeat',
            backgroundColor: (t) =>
              t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
          <Box
            sx={{
              my: 25,
              mx: 4,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: 'secondary.main', backgroundImage: 'url(https://i.redd.it/1ka2cmdk35u91.jpg)' }}>
              <SurfingIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              It's Time to Shred
            </Typography>
            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
              <Search />
              
            </Box>
          </Box>
        </Grid>
      </Grid>

      <Grid>

        

      </Grid>

    </ThemeProvider>
  );
}