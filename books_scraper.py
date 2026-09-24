"""Scrape book titles, prices, and availability from Books to Scrape."""

from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "books.csv"
HEADERS = {"User-Agent": "web-scraping-python/1.0"}


def scrape_books() -> list[dict[str, str]]:
    """Return book details from the first Books to Scrape page."""
    response = requests.get(URL, headers=HEADERS, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for book in soup.select("article.product_pod"):
        books.append(
            {
                "book_name": book.select_one("h3").get_text(strip=True),
                "book_price": book.select_one("p.price_color").get_text(strip=True),
                "book_availability": book.select_one(
                    "p.instock.availability"
                ).get_text(" ", strip=True),
            }
        )
    return books


def main() -> None:
    books = pd.DataFrame(scrape_books())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    books.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(books.to_string(index=False))
    print(f"\nSaved {len(books)} books to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
