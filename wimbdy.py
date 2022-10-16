import requests
import csv

LAT = "25.77481"
LONG = "-81.19773"
combo = LAT + "," + LONG


url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

querystring = {"aggregateHours":"24","location":combo,"contentType":"csv","unitGroup":"us","shortColumnNames":"1"}

headers = {
	"X-RapidAPI-Key": "6520434f99mshb47aa5f323c8a54p16f385jsn176f39a1c3c6",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}


response = requests.request("GET", url, headers=headers, params=querystring)

print(response)
print(type(response))
print(response.apparent_encoding)


decoded_content = response.content.decode('utf-8')

cr = csv.reader(decoded_content.splitlines(), delimiter=',')
my_list = list(cr)
for row in my_list:
    print(row)


