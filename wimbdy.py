import requests
import json

LAT = "25.77481"
LONG = "-81.19773"
combo = LAT + "," + LONG


url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

querystring = {"aggregateHours":"24","location":combo,"contentType":"json","unitGroup":"us","shortColumnNames":"1"}

headers = {
	"X-RapidAPI-Key": "6520434f99mshb47aa5f323c8a54p16f385jsn176f39a1c3c6",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}

#testStr = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/38.9697,-77.385?key=6520434f99mshb47aa5f323c8a54p16f385jsn176f39a1c3c6"

response = requests.request("GET", url, headers=headers, params=querystring)
#response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/38.9697,-77.385?key=6520434f99mshb47aa5f323c8a54p16f385jsn176f39a1c3c6")

print(response)
print(type(response))
print(response.apparent_encoding)
jRes = response.json()

print(jRes.keys())





