# Web Scraping with Python

A practical collection of Python web-scraping examples using **Requests**, **BeautifulSoup**, **Pandas**, **lxml**, and **OpenPyXL**. The project turns public web pages into structured datasets through three focused examples: books, inspirational quotes, and football match results.


## Project Overview

This project demonstrates a beginner-friendly scraping workflow from request to export. Each script sends an HTTP request to a public practice website, parses the returned HTML, extracts selected fields, stores the results in a Pandas DataFrame, and saves the data locally.

The examples intentionally use educational scraping websites and a public sports website. They show how the same core process can be adapted to different page structures, including product cards, quote blocks, and nested match cards.

## Technologies Used

- **Python** for scripting and automation.
- **Requests** for downloading HTML pages.
- **BeautifulSoup** for parsing and extracting information from HTML.
- **Pandas** for tabular data handling and CSV export.
- **lxml** as the HTML parser used by the YallaKora scraper.
- **OpenPyXL** for writing match results to an Excel workbook.

## Project Structure

```text
web-scraping-python/
│
├── books_scraper.py
├── quotes_scraper.py
├── yallakora_scraper.py
│
├── output/
│   ├── books.csv
│   ├── quotes.csv
│   └── matches.xlsx
│
├── images/
│   ├── books-scraper.png
│   ├── quotes-scraper.png
│   └── yallakora-scraper.png
│
├── requirements.txt
└── README.md
```

The `output/` files are generated when the scripts run. They are not required before the first execution.

## 1. Books to Scrape

![Books Web Scraper](images/books-scraper.png)

`books_scraper.py` collects the first page of the [Books to Scrape](https://books.toscrape.com/) practice website. For each book, it extracts the title, price, and availability status, then saves the results to `output/books.csv`.

Run it with:

```bash
python books_scraper.py
```

## 2. Quotes to Scrape

![Quotes Web Scraper](images/quotes-scraper.png)

`quotes_scraper.py` extracts quote text, author names, and keyword tags from the first page of the [Quotes to Scrape](https://quotes.toscrape.com/) practice website. The structured data is saved to `output/quotes.csv`.

Run it with:

```bash
python quotes_scraper.py
```

## 3. YallaKora Match Scraper

![YallaKora Match Scraper](images/yallakora-scraper.png)

`yallakora_scraper.py` accepts a match date in `MM/DD/YYYY` format and requests the corresponding [YallaKora match-center](https://www.yallakora.com/match-center) page. It extracts championship names, team names, final scores, and match times for finished matches, then saves the results to `output/matches.xlsx`.

Run it with:

```bash
python yallakora_scraper.py
```

When prompted, enter a date such as:

```text
01/15/2026
```

## How to Run

1. Clone the repository and move into the project directory:

   ```bash
   git clone https://github.com/youmna24zaian/web-scraping-python.git
   cd web-scraping-python
   ```

2. Create and activate a virtual environment if desired:

   ```bash
   python -m venv .venv
   ```

   On macOS and Linux:

   ```bash
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run any scraper from the project root:

   ```bash
   python books_scraper.py
   python quotes_scraper.py
   python yallakora_scraper.py
   ```

## Learning Objectives

This project is designed to help learners practice how to:

- Send HTTP requests and handle responses.
- Parse HTML with CSS selectors and BeautifulSoup.
- Identify useful page elements and extract clean text.
- Transform scraped records into structured Python dictionaries.
- Create Pandas DataFrames from scraped data.
- Export tabular results to CSV and Excel formats.
- Work with different HTML layouts and nested page components.
- Add basic validation, request timeouts, and error handling to a scraper.

## Disclaimer

This repository is intended for educational purposes. Before scraping any website, review its terms of service, robots.txt guidance, rate limits, and applicable laws. Use responsible request rates, collect only information that you are permitted to access, and do not use these scripts to bypass authentication, access controls, or other technical restrictions. Website layouts and URLs can change, so a scraper may require maintenance over time.

## Author

**Youmna Zaian** · [GitHub](https://github.com/youmna24zaian)

## References

[1]: https://books.toscrape.com/ "Books to Scrape practice website"
[2]: https://quotes.toscrape.com/ "Quotes to Scrape practice website"
[3]: https://www.yallakora.com/match-center "YallaKora match center"
