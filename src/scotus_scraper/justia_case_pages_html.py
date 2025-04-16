import requests
from bs4 import BeautifulSoup
import json
import os
from concurrent.futures import ProcessPoolExecutor
import itertools
from scotus_scraper.config import CASELIST, JUSTIA_URL, JUSTIA_CASE_PAGES_DIR

def get_page(url, output_dir):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')

  html_file = '_'.join(url.split('/')[-6:-1]) + '.html'
  output_file = os.path.join(output_dir, html_file)

  with open(output_file, 'w', encoding='utf-8') as file:
    file.write(page.text)

  return output_file

def main():
  case_file = CASELIST
  url_base = JUSTIA_URL
  output_dir = JUSTIA_CASE_PAGES_DIR

  with open(case_file, 'r') as json_file:
    cases = json.load(json_file)

  args = [(url_base + case['url'], output_dir) for case in cases]

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Directory '{output_dir}' created.")

  with ProcessPoolExecutor() as executor:
    results = list(itertools.starmap(get_page, args))

if __name__ == "__main__":
  main()

