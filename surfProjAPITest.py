

import requests

r = requests.get('https://api.usa.gov/crime/fbi/sapi/api/data/supplemental/not-specified/states/CA/OFFENSE/2000/2022?')

print(dir(r))