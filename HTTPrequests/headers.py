import requests

url = "https://icanhazdadjoke.com/"

res = requests.get(url, headers={"Accept": "application/json"})

print(res.text)  # this is a string
print(res.json())  # this is a object

data = res.json()

data["joke"]  # can take the value of key "joke"
