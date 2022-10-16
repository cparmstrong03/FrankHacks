beaches = {
    'Kaimu Black Sand Beach, HI': [(19.356697, -154.968307), 0],
    'Glass Beach, CA':	[(39.452717,	-123.813866), 0],
    'Siesta Key Beach, FL':	[(27.265862,	-82.552521), 0],
    "Marshall's Beach, CA":	[(37.801685,	-122.479965), 0],
    'Honokalani Beach, HI':	[(20.787159,	-156.002045), 0],
    'Mauna Kea Beach, HI':	[(20.005039,	-155.824615), 0],
    'North Myrtle Beach, SC': [(33.850655,	-78.654381), 0],
    'Edisto Island Beach, SC':	[(32.477474,	-80.335297), 0],
    'Cedar Beach, NY':	[(40.630100,	-73.340958), 0],
    'Sebastian Beach Inn, FL':	[(27.935509,	-80.490044), 0],
    'Potomac Standing Wave, MD':	[(38.949848,	-77.127647), 0],
    'Ortley Beach, Toms River, NJ':	[(39.955673,	-74.074303), 0],
    'Trump International Beach Resort, FL':	[(25.942871,	-80.123383), 0],
    'Sunset Beach, FL':	[(27.745003,	-82.759659), 0],
    'Chapman Point, Cannon Beach, OR':	[(45.908997,	-123.968475), 0],
    'Haulover Beach, FL':	[(25.912266,	-80.121277), 0],
    'Beach & Boardwalk, Seaside Park, NJ':	[(39.926064,	-74.073860), 0],
    'Ocean Isle Beach, NC':	[(33.905758,	-78.391144), 0],
    'Mutiny Bay, WA':	[(47.993195,	-122.561462), 0]
}

def beach_location(beachname):
    return beaches[beachname][0]

def beach_direction(beachname):
    return beaches[beachname][1]

def diff_in_directions(beach_name, windspeed, winddir):
    beachdir = beach_location(beach_name)




