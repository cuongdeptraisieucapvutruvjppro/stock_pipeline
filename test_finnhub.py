import requests

API_KEY = "davia5hr01qp1e4o6etgdavia5hr01qp1e4o6eu0"

url = f"https://finnhub.io/api/v1/quote?symbol=AAPL&token={API_KEY}"

response = requests.get(url)

print(response.status_code)
print(response.json())