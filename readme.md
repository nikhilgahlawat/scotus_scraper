# About
A project to scrape opinions, briefs, and other documents from the United States Supreme Court and make them available in machine-readable datasets.

Data scraped from [Justia](https://supreme.justia.com/), [Oyez](https://www.oyez.org/), and the [US Supreme Court](https://www.supremecourt.gov/).

A little more background on the idea for the project [here](https://www.nikhilgahlawat.com/projects/scotus-scraper/).

# Setup

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

# Running Scripts

To run the entire flow:
  ```sh
  run-all
  ```

When run it will scrape text from opinions as well as metadata on briefs, filings, and oral arguments. All files will be saved locally.

Hoping to add text data from briefs as well.

By default, the project scrapes data from 2020 to 2024. To adjust this window, update the `START_YEAR` and `END_YEAR` fields in [`config.py`](https://github.com/nikhilgahlawat/scotus_scraper/blob/main/src/scotus_scraper/config.py)

# Other Resources
Here are some other useful resources I found while researching this project:
- [Supreme Court Database](http://scdb.wustl.edu/) from Washington University Law
 - [Caselaw Access Project](https://case.law/) from Harvard Law School
 - [Supreme Court Oral Arguments Corpus](https://convokit.cornell.edu/documentation/supreme.html) from ConvoKit made by researchers at Cornell
 - [Supreme Court Data](https://free.law/projects/supreme-court-data) from [Free Law Project](https://free.law/) and [CourtListener](https://www.courtlistener.com/)

