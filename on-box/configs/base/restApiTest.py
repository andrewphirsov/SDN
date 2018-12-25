import requests

url = "https://api.icndb.com/jokes/random"

payload = ""
headers = {
    'Accept': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "fd7096d8-48e8-4f5d-aaae-246665338261"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)