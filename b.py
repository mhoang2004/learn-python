# import calendar

# yy = 2004
# mm = 2
# print(calendar.month(yy, mm))

from random import choice
import requests

all_quotes = []

quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote: ")
print(quote["text"])
guess = ''
while guess.lower() != quote["author"].lower() and remaining_guesses:
    guess = input(
        f"Who said this quote? Guesses remaining: {remaining_guesses}. ")
    if guess.lower() != quote["author"].lower():
        print("You it right!")
        break
    remaining_guesses -= 1
    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(
            f"Here's a hint: The author was born on {birth_date} {birth_place}")
    elif remaining_guesses == 2:
        print(
            f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(
            f"Here's a hint: THe author's last name starts with: {last_initial}")
    else:
        print(
            f"Sorry you ran out of guesses. The answer was {quote['author']}")
