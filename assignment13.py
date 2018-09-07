import requests
response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&json=?")
data=response.json()
print(data["quoteText"])
