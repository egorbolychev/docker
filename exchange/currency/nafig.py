import requests

url = "https://api.apilayer.com/exchangerates_data/latest"

payload = {
  'symbols': '',
  'base': 'USD'
}
headers = {
  "apikey": "0G61uJfxj02q8S841GPAoPZeUOC6up7J"
}

response = dict(requests.request("GET", url, headers=headers, params=payload).json()['rates'])
response_list = tuple([(a, b) for b, a in dict.items(response)])
print(response_list)
