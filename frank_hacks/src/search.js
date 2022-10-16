/* eslint-disable no-use-before-define */
import React from "react";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";

export default function Search() {
  function handleInputChange(event, value) {
    for (let i = 0; i < beaches.length; i++) {
      if (value === beaches[i])
        JSON.stringify(value);
    }
  }

  return (
    <Autocomplete
      id="combo-box-demo"
      options={beaches}
      getOptionLabel={option => option}
      style={{ width: 300 }}
      onInputChange={handleInputChange}
      renderInput={params => (
        <TextField {...params} label="Find Your Beach" variant="outlined" fullWidth />
      )}
    />
  );
}

// Top 100 films as rated by IMDb users. http://www.imdb.com/chart/top
const beaches = [
  'Kaimu Black Sand Beach, HI',
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
  'Mutiny Bay, WA'
];
