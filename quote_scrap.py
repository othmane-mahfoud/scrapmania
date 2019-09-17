import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
all_quotes = []
base_url = "http://quotes.toscrape.com"
page_param = "/page/1"

while page_param:
    response = requests.get(f"{base_url}{page_param}")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    for q in quotes:
        text = q.find(class_="text").get_text()
        author = q.find("small").get_text()
        link_to_bio = q.find("a")["href"]
        all_quotes.append({
            "text": text,
            "author": author,
            "link": link_to_bio
        })
    next_btn = soup.find(class_="next")
    page_param = next_btn.find("a")["href"] if next_btn else None
    sleep(2)

quote = choice(all_quotes)
num_guesses = 4
guess = ''
print(quote["text"])
while guess.lower() != quote["author"].lower() and num_guesses != 0:
    if num_guesses == 3:
        res = requests.get(f"{base_url}{quote['link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        print(f"The author was born in {birth_date}")
    guess = input(f"{num_guesses} guesses remaining: Who said this quote ? : ")
    num_guesses -= 1