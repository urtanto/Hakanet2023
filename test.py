import json

import requests

# url = "http://127.0.0.1:8000/signup"
# data = {"username": "vasya",
#         "password": "promprog"}
# r = requests.post(url, data=data)

# url = "http://127.0.0.1:8000/login"
# r = requests.post(url, data=data)
# context: dict = json.loads(r.content)
# token = context["token"]

# url = "http://127.0.0.1:8000/test"
# r = requests.get(url, headers={"Authorization": f"Token {'c2061738ddcfbed3de6522a14b32e8813f55896a'}"})
# context: dict = json.loads(r.content)

# url = "http://127.0.0.1:8000/image_upload"
# files = {"file": open("/home/urtanto/Downloads/9f8fdff471b7d281f81f694c100b5adc.png", mode="rb")}
# token = "0f68538d5fc25b8ad6529ae6fe94111fbef50305"
# r = requests.post(url, files=files, headers={"Authorization": f"Token {token}"})

url = "http://127.0.0.1:8000/review/create"
date = {"text": "dsdfgsdfgs"}
token = "0f68538d5fc25b8ad6529ae6fe94111fbef50305"
r = requests.post(url, data=date, headers={"Authorization": f"Token {token}"})
print(r.text)
