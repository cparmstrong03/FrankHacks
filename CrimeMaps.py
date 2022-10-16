import requests

url = "https://instagram47.p.rapidapi.com/user_following"

querystring = {"userid":"1718924098"}

headers = {
	"X-RapidAPI-Key": "f99e001d27mshdbff5f6c6372b98p13cecfjsn6d862349dfc0",
	"X-RapidAPI-Host": "instagram47.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)