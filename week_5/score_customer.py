import requests

url = 'http://0.0.0.0:9697/predict'
customer = {
    "contract": "two_year",
    "tenure": 1,
    "monthlycharges": 10}


print(requests.post(url, json=customer).json())