import pdfplumber
import json
import requests
from io import BytesIO
from concurrent.futures import ProcessPoolExecutor
import logging
from scotus_scraper.config import AMICUS_BRIEFS_LIST, AMICUS_BRIEFS_TEXT


logging.basicConfig(
  filename = 'pdf_processing.log',
  level = logging.INFO,
  format = '%(asctime)s:%(levelname)s:%(message)s'
  )

def download_pdf(url):
  response = requests.get(url)
  response.raise_for_status()
  return BytesIO(response.content)

def extract_text_from_pdf(pdf_file):
  full_text = []

  try:
    with pdfplumber.open(pdf_file) as pdf:
      for page in pdf.pages:
        page_number = page.page_number
        text = page.extract_text()
        full_text.append({
          'page': page_number,
          'text': text
        })
    return full_text
  except Exception as e:
    logging.error(f'Error processing {pdf_file}: {e}')

def is_valid_pdf(file):
  try:
    with pdfplumber.open(file) as pdf:
      pdf.pages[0]
    return True
  except Exception as e:
    logging.error(f'Invalid PDF: {e}')
    return False


def download_and_extract(url):
  file = download_pdf(url)
  if is_valid_pdf(file):
    return extract_text_from_pdf(file)
  else:
    logging.warning(f"The file from {url} is not a valid PDF. Skipping.")
    return None


def main(input_file, output_file):
  with open(input_file, 'r') as json_file:
    amicus_briefs = json.load(json_file)

  urls = [item['url'] for item in amicus_briefs]

  with ProcessPoolExecutor() as executor:
    results = list(executor.map(download_and_extract, urls))

  for meta, text in zip(amicus_briefs, results):
    meta['text'] = text

  with open(output_file, 'w') as json_file:
    json.dump(amicus_briefs, json_file, indent=2)


if __name__ == "__main__":
  input_file = AMICUS_BRIEFS_LIST
  output_file = AMICUS_BRIEFS_TEXT
  main(input_file, output_file)

