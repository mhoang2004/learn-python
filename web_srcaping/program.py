import requests
from bs4 import BeautifulSoup
import csv

# url = "hhttps://www.rithmschool.com/blog/"
url = "https://dantri.com.vn/"

response = requests.get(url)

# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.select(".article-hot article")

# print(articles)

with open("dantri_data.csv", "w", encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["title", "url"])

    for article in articles:
        title = article.find("h3").get_text()
        url = article.find("h3").a["href"]
        csv_writer.writerow([title, url])
