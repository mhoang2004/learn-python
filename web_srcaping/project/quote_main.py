import requests
from bs4 import BeautifulSoup
import json
from random import choice

# url = 'http://quotes.toscrape.com'
# respone = requests.get(url)
# soup = BeautifulSoup(respone.text, "html.parser")
# quotes = soup.select(".quote")

# while(True):
#     next_url = soup.find(attrs={"class": "next"})
#     if not next_url:
#         break

#     respone = requests.get(url + next_url.a["href"])
#     soup = BeautifulSoup(respone.text, "html.parser")

#     quotes.extend(soup.select(".quote"))

# objs = []


# for quote in quotes:
#     text = quote.find(attrs={"class": "text"}).get_text()
#     author_name = quote.find(attrs={"class": "author"}).get_text()

#     #take the url of author information
#     url_author = quote.find(attrs={"class": "author"}).find_next_sibling()["href"]

#     author_respone = requests.get(url + url_author)
#     author_soup = BeautifulSoup(author_respone.text, "html.parser")

#     author_born_date = author_soup.find(attrs={"class": "author-born-date"}).text
#     author_born_location = author_soup.find(attrs={"class": "author-born-location"}).text

#     author_info = "Born: " + author_born_date + " " + author_born_location

#     obj = {
#         "text": text,
#         "author": author_name,
#         "authorInfo": author_info
#     }

#     objs.append(obj)

# with open("quotes.json", "w") as file:
#     frozen = json.dumps(objs)
#     file.write(frozen)

with open("quotes.json") as file:
    content = file.read()
    data = json.loads(content)

play_again = "y"
while (play_again == "y"):
    the_choosen = choice(data)
    guess_num = 4

    def hint(num):
        if num == 3:
            print("Here's a hint: The author was " + the_choosen["authorInfo"])
        elif num == 2:
            print(
                f"Here's a hint: The author's first name starts with {the_choosen['author'][0]}")
        elif num == 1:
            print(f"No hint kakaka")

    print("Here's a quote: \n\n")
    print(the_choosen["text"])

    while (guess_num):
        user_input = input(
            f"\n\nWho said this? Guesses remaining: {guess_num}. ")

        if user_input.lower() == the_choosen["author"].lower():
            print("You guessed correctly! Congratulations!")
            break
        else:
            guess_num -= 1
            hint(guess_num)

    if guess_num == 0:
        print(
            f"Sorry, you've run out of guesses. The answer was `{the_choosen['author']}`")

    play_again = input("Would you like to play again (y/n) ? ")
    if play_again != "y":
        print("OK! See you next time!")
