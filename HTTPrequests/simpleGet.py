import requests

# url = "https://google.com"
url = "https://icanhazdadjoke.com/"

res = requests.get(url)

print(res)  # <Response [200]>
# print(res.ok)  # True
# print(res.headers)
# print(res.text)  # HTML file
