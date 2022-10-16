

import requests

r = requests.get('https://api.windy.com/api/point-forecast/v2')

print(dir(r))