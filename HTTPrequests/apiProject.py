import requests
import random
import pyfiglet

header = pyfiglet.figlet_format("DAD JOKE 3000!")
print(header)

user_input = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    # is telling the server that the client expects to receive a JSON response.
    headers={"Accept": "application/json"},
    params={
        "term": user_input,
    }
)

data = response.json()
# print(data["results"])

data_length = len(data["results"])

if (data_length == 0):
    print(
        f"Sorry, I don't have any jokes about `{user_input}`! Please try again.")
elif (data_length == 1):
    print(f"I've got one joke about `{user_input}`. Here it is: ")
    print(data["results"][0]["joke"])
else:
    print(
        f"I've got {data_length} joke about `{user_input}`. Here it is: ")
    randomNum = random.randint(0, data_length - 1)
    print(data["results"][randomNum]["joke"])
