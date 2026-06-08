import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "hour": 14,
    "dayofweek": 2,
    "month": 6,
    "year": 2025,
    "lag1": 25000,
    "lag24": 24000,
    "lag168": 23000
}

response = requests.post(url, json=data)

print(response.json())