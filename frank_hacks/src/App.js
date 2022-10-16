import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import SurfingIcon from '@mui/icons-material/Surfing';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme();

export default function Locate() {
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      text: data.get('text')
    });
  };

  beaches = ['Kaimu Black Sand Beach, HI',
  'Glass Beach, CA',
  'Siesta Key Beach, FL',
  'Marshall\'s Beach, CA',
  'Honokalani Beach, HI',
  'Mauna Kea Beach, HI',
  'North Myrtle Beach, SC',
  'Edisto Island Beach, SC',
  'Cedar Beach, NY',
  'Sebastian Beach Inn, FL',
  'Potomac Standing Wave, MD',
  'Ortley Beach, Toms River, NJ',
  'Trump International Beach Resort, FL',
  'Sunset Beach, FL',
  'Chapman Point, Cannon Beach, OR',
  'Haulover Beach, FL',
  'Beach & Boardwalk, Seaside Park, NJ',
  'Ocean Isle Beach, NC',
  'Mutiny Bay, WA']

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
            backgroundImage: 'url(https://wallpaperaccess.com/full/1540066.jpg)',
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
              my: 22,
              mx: 4,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
              <SurfingIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              It's Time to Shred
            </Typography>
            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="text"
                label="Find Your Beach"
                name="text"
                autoComplete="text"
                autoFocus
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Locate
              </Button>
              
            </Box>
          </Box>
        </Grid>
      </Grid>

      <Grid>

        

      </Grid>

    </ThemeProvider>
  );
}