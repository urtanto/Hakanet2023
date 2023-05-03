import requests

response = requests.request("POST", "http://127.0.0.1:8000/login/", data={"username": "vasya",
                                                                         "password": "promprog"})
print(response.text)
print(response.status_code)
response = requests.request("GET", "http://127.0.0.1:8000/check/")
print(response.text)
print(response.status_code)