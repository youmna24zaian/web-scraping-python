# Web Scraping with Python

![Web Scraping with Python project cover](images/web_scraping_cover_variant_a.png)

This repository demonstrates a practical workflow for turning web pages into structured, reusable data with Python.

A practical collection of Python web-scraping examples using **Requests**, **BeautifulSoup**, **Pandas**, **lxml**, and **OpenPyXL**. The project separates the original notebook code into three standalone scripts without changing the scraping logic.


## Project Overview

This project demonstrates how to request web pages, parse their HTML, extract selected information, print the results, and save football match data to an Excel file. The examples cover books, inspirational quotes, and football match results.

The three scripts are intentionally kept simple and focused on demonstrating the core steps of a basic web-scraping workflow.

## Technologies Used

- **Python** for scripting.
- **Requests** for downloading web pages.
- **BeautifulSoup** for parsing HTML.
- **Pandas** for creating a DataFrame from match results.
- **lxml** as the parser used for the YallaKora page.
- **OpenPyXL** through Pandas for Excel export.

## Project Structure

```text
web-scraping-python/
│
├── books_scraper.py
├── quotes_scraper.py
├── yallakora_scraper.py
│
├── images/
│   ├── project-cover.png
│   ├── books-scraper.png
│   ├── quotes-scraper.png
│   └── yallakora-scraper.png
│
├── requirements.txt
└── README.md
```

The YallaKora script generates matches1.xlsx in the project directory when it runs.

## 1. Books to Scrape

![Books Web Scraper](images/books-scraper.png)

The `books_scraper.py` script requests the first page of [Books to Scrape](https://books.toscrape.com/). It finds each `product_pod` article and prints the book name, price, and availability.

Run it with:

```bash
python books_scraper.py
```

## 2. Quotes to Scrape

![Quotes Web Scraper](images/quotes-scraper.png)

The `quotes_scraper.py` script requests the first page of [Quotes to Scrape](https://quotes.toscrape.com/). It collects the quote text, author, and tags into a list of dictionaries, then prints that list.

Run it with:

```bash
python quotes_scraper.py
```

## 3. YallaKora Match Scraper

![YallaKora Match Scraper](images/yallakora-scraper.png)

The `yallakora_scraper.py` script asks the user for a match date and requests the corresponding [YallaKora match-center](https://www.yallakora.com/match-center) page. It extracts championship names, finished matches, team names, match results, scores, and match times. The results are converted into a Pandas DataFrame, printed, and saved as `matches1.xlsx`.

Run it with:

```bash
python yallakora_scraper.py
```

When prompted, enter the date in the format expected by the original script, such as:

```text
01/15/2026
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/youmna24zaian/web-scraping-python.git
   cd web-scraping-python
   ```

2. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Run any of the three scripts:

   ```bash
   python books_scraper.py
   python quotes_scraper.py
   python yallakora_scraper.py
   ```

On some systems, use `python3` and `pip3` instead of `python` and `pip`.

## Learning Objectives

This project provides hands-on practice with:

* Sending HTTP requests and retrieving web pages.
* Parsing HTML using BeautifulSoup and lxml.
* Selecting page elements and extracting text and attributes.
* Organizing extracted data using Python lists and dictionaries.
* Creating structured datasets with Pandas DataFrames.
* Exporting tabular data to Excel.
* Understanding the basic workflow of collecting and preparing web data for further analysis.

## Disclaimer

This repository is intended for educational purposes. Before scraping any website, review its terms of service, robots.txt guidance, rate limits, and applicable laws. Use responsible request rates, collect only information that you are permitted to access, and do not use these scripts to bypass authentication, access controls, or other technical restrictions. Website layouts and URLs can change, so a scraper may require maintenance over time.

## Author

**Youmna Zaian** ·

## Learning Context

This project was developed as a practical application of concepts covered during my Data Science training.

It focuses on applying Python and web scraping techniques through hands-on implementation, including collecting, parsing, and organizing data from web pages.
