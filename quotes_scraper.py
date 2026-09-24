import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
  url = "https://quotes.toscrape.com/"

  page = requests.get(url)

  soup = BeautifulSoup(page.content, "html.parser")

  quotes = soup.find_all("div", {"class" : "quote"})

  quotes_list = []

  for quote in quotes:
    text = quote.find("span", {"class" : "text"}).text.strip()
    by = quote.find("small").text.strip()
    Tags = quote.find("meta", {"class" : "keywords"}).get("content")

    quotes_data = {"text":text,
                       "by":by,
                       "Tags": Tags}

    quotes_list.append(quotes_data)

  print(quotes_list)

main()
