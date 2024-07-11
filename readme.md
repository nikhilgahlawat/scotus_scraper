# About
A project to scrape opinions, briefs, and other data from the United States Supreme Court.

Data scraped from [Justia](https://supreme.justia.com/), [Oyez](https://www.oyez.org/), and the [US Supreme Court](https://www.supremecourt.gov/).


## Setup

1. Clone the repository:
  ```sh
  git clone https://github.com/nikhilgahlawat/scotus_scraper.git
  cd scotus_scraper
  ```

2. Create and activate a virtual environment:
  ```sh
  python -m venv venv
  source venv/bin/activate # On Mac
  ```

3. Install the dependencies:
  ```sh
  pip install -r requirements.txt
  ```

4. Install the project:
  ```sh
  pip install -e .
  ```

## Running Scripts

To run the entire flow:
  ```sh
  run-all
  ```

When run it will scrape text from opinions as well as metadata on briefs, filings, and oral arguments. All files will be saved locally.

Hoping to add text data from briefs as well.

By default, the project scrapes data from 2020 to 2024. To adjust this window, update the `START_YEAR` and `END_YEAR` fields in [`config.py`](https://github.com/nikhilgahlawat/scotus_scraper/blob/main/src/scotus_scraper/config.py)
