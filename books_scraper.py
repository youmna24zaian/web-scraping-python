import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
  url = "https://books.toscrape.com/"

  page = requests.get(url)

  # PARSE THE HTML USING BEAUTIFULSOUP
  soup = BeautifulSoup(page.content, "html.parser")

  books = soup.find_all("article", {"class" : "product_pod"})

  for book in books:
    book_name = book.find("h3").text.strip()

    book_price = book.find("p", {"class" : "price_color"}).text.strip()

    book_availability = book.find("p", {"class" : "instock availability"}).text.strip()

    print(book_name, book_price, book_availability)

main()
