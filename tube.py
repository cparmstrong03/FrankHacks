beaches = {
    'Kaimu Black Sand Beach, HI': [[19.356697, -154.968307], 0],
    'Glass Beach, CA':	[[39.452717,	-123.813866], 0],
    'Siesta Key Beach, FL':	[[27.265862,	-82.552521], 0],
    "Marshall's Beach, CA":	[[37.801685,	-122.479965], 0],
    'Honokalani Beach, HI':	[[20.787159,	-156.002045], 0],
    'Mauna Kea Beach, HI':	[[20.005039,	-155.824615], 0],
    'North Myrtle Beach, SC': [[33.850655,	-78.654381], 0],
    'Edisto Island Beach, SC':	[[32.477474,	-80.335297], 0],
    'Cedar Beach, NY':	[[40.630100,	-73.340958], 0],
    'Sebastian Beach Inn, FL':	[[27.935509,	-80.490044], 0],
    'Potomac Standing Wave, MD':	[[38.949848,	-77.127647], 0],
    'Ortley Beach, Toms River, NJ':	[[39.955673,	-74.074303], 0],
    'Trump International Beach Resort, FL':	[[25.942871,	-80.123383], 0],
    'Sunset Beach, FL':	[[27.745003,	-82.759659], 0],
    'Chapman Point, Cannon Beach, OR':	[[45.908997,	-123.968475], 0],
    'Haulover Beach, FL':	[[25.912266,	-80.121277], 0],
    'Beach & Boardwalk, Seaside Park, NJ':	[[39.926064,	-74.073860], 0],
    'Ocean Isle Beach, NC':	[[33.905758,	-78.391144], 0],
    'Mutiny Bay, WA':	[[47.993195,	-122.561462], 0],
    'Ocean Beach, CA': [[32.7495, 117.2470], 0],
    'Long Beach, NY': [[40.5884, 73.6579], 0],
    'Fort Cronkite/Rodeo Beach, CA': [[37.8326, 122.5349], 0],
    'Pacifica Beach, CA': [[37.5989, 122.5019], 0],
    'Bolinas, CA': [[37.9069, 122.6825], 0],
    'Stinson Beach, CA': [[37.9005, 122.6444], 0],
    'Fort Point, CA': [[37.8106, 122.4771], 0],
    'Gilgo Beach, NY': [[40.6184, 73.3976], 0],
    'Point Lookout Beach, NY': [[40.5922, 73.5763], 0]
}

def beach_location(beachname):
    return beaches[beachname][0]

def beach_direction(beachname):
    return beaches[beachname][1]

def diff_in_directions(beach_name, winddir):
    beachdir = beach_direction(beach_name)
    return abs(beachdir - winddir)

onshore_windmarkers = [0, 30, 30+35, 90]
onshore_scoremarkers = [2.9, 2.6, 1.4, 1.0]

offshore_windmarkers = [180.0, 180.0-30, 180-30-17.5, 90]
offshore_scoremarkers = [5.0, 4.0, 3.2, 1.0]


def winddirection_rating(beachname, winddirection):
    dirdiff = diff_in_directions(beachname, winddirection)
    dirdiff = (dirdiff + 180) % 360
    if dirdiff <= 90:
        for i in range(len(onshore_scoremarkers)- 1):
            lowerboundwind = onshore_windmarkers[i]
            upperboundwind = onshore_windmarkers[i+1]
            if (dirdiff >= lowerboundwind and dirdiff <= upperboundwind):
                lowerboundscore = onshore_scoremarkers[i]
                upperboundscore = onshore_scoremarkers[i+1]

                windboundsdiff = upperboundwind - lowerboundwind
                difffraction = (dirdiff - lowerboundwind) / windboundsdiff
                return lowerboundscore + ((upperboundscore - lowerboundscore) * difffraction)

    elif (dirdiff > 90 and dirdiff < 181):
        for i in range(len(offshore_scoremarkers) - 1):
            upperboundwind = offshore_windmarkers[i]
            lowerboundwind = offshore_windmarkers[i+1]
            if (dirdiff <= upperboundwind and dirdiff >= lowerboundwind):
                upperboundscore = offshore_scoremarkers[i]
                lowerboundscore = offshore_scoremarkers[i+1]
                
                windboundsdiff = upperboundwind - lowerboundwind
                updirdiff = upperboundwind - dirdiff
                difffraction = updirdiff/windboundsdiff
                return upperboundscore - ((upperboundscore - lowerboundscore) * difffraction)
    
    else:
        print('DEBUG: Something has gone wrong brotha, and the dirdiff is greater than 180')

def windspeed_rating(windspeed):
    rating = (-0.0000222107 * windspeed**4) + (0.00168262 * windspeed**3) - (0.0382879 * windspeed**2) + (0.0776512 * windspeed) + 5
    return max(0.25, rating)

def weight_of_windspeed(windspeed):
    weight = ((-8.430860941587*10**(-9)) * windspeed**8) + ((9.28381296709*10**(-7)) * windspeed**7) - (0.0000397973 * windspeed**6) + (0.000841596 * windspeed**5)
    weight += (-0.0091662 * windspeed**4) + (0.0490661 * windspeed**3) - (0.115177 * windspeed**2) + (0.0604123 * windspeed) + 0.994062
    return min(weight, 0.99)

def final_rating(beachname, winddirection, windsspeed):
    wd_rating = winddirection_rating(beachname, winddirection)
    ws_rating = windspeed_rating(windsspeed)
    ws_weight = weight_of_windspeed(windsspeed)
    return ((1-ws_weight) * wd_rating) + (ws_weight * ws_rating)

