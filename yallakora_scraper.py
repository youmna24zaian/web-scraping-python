"""Scrape finished football matches from YallaKora by date."""

from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.yallakora.com/match-center"
OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "matches.xlsx"
HEADERS = {"User-Agent": "web-scraping-python/1.0"}


def normalize_date(date_text: str) -> str:
    """Validate a date and return it in the format expected by YallaKora."""
    parsed_date = datetime.strptime(date_text.strip(), "%m/%d/%Y")
    return parsed_date.strftime("%m/%d/%Y")


def scrape_matches(date_text: str) -> list[dict[str, str]]:
    """Return finished matches grouped by championship for a selected date."""
    date = normalize_date(date_text)
    response = requests.get(
        BASE_URL,
        params={"date": date},
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    matches = []
    for championship in soup.select("div.matchCard"):
        championship_title = championship.select_one("h2")
        if championship_title is None:
            continue

        for match in championship.select("div.item.finish.liItem"):
            team_a = match.select_one("div.teams.teamA p")
            team_b = match.select_one("div.teams.teamB p")
            result = match.select_one("div.MResult")
            scores = result.select("span.score") if result else []
            time = result.select_one("span.time") if result else None

            if not team_a or not team_b or len(scores) < 2:
                continue

            matches.append(
                {
                    "championship_name": championship_title.get_text(strip=True),
                    "team_a": team_a.get_text(strip=True),
                    "team_b": team_b.get_text(strip=True),
                    "score": f"{scores[0].get_text(strip=True)} - {scores[1].get_text(strip=True)}",
                    "time": time.get_text(strip=True) if time else "",
                }
            )
    return matches


def main() -> None:
    date_text = input("Enter the match date (MM/DD/YYYY): ")
    matches = pd.DataFrame(scrape_matches(date_text))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    matches.to_excel(OUTPUT_PATH, index=False)
    print(matches.to_string(index=False))
    print(f"\nSaved {len(matches)} matches to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
