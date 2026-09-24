"""Scrape quote text, authors, and tags from Quotes to Scrape."""

from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"
OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "quotes.csv"
HEADERS = {"User-Agent": "web-scraping-python/1.0"}


def scrape_quotes() -> list[dict[str, str]]:
    """Return quote text, author, and tags from the first page."""
    response = requests.get(URL, headers=HEADERS, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []
    for quote in soup.select("div.quote"):
        quotes.append(
            {
                "text": quote.select_one("span.text").get_text(strip=True),
                "author": quote.select_one("small.author").get_text(strip=True),
                "tags": quote.select_one("meta.keywords").get("content", ""),
            }
        )
    return quotes


def main() -> None:
    quotes = pd.DataFrame(scrape_quotes())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    quotes.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(quotes.to_string(index=False))
    print(f"\nSaved {len(quotes)} quotes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
