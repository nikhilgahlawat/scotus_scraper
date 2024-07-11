import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import json
from concurrent.futures import ProcessPoolExecutor
from scotus_scraper.config import JUSTIA_YEAR_URL, START_YEAR, END_YEAR, CASELIST, DATA_DIR

def process_page(url):
  print('Parsing', url)

  caselist = []
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')

  blocks = soup.find_all('div', class_='has-padding-content-block-30 -zb search-result')

  for block in blocks:
    name = block.find('a', class_='case-name').get_text().strip()
    url = block.find('a', class_='case-name').get('href')
    docket = re.findall("Docket Number: (.*)", block.get_text())[0]
    date = re.findall("Date: (.*)", block.get_text())[0]
    volume = url.split('/')[-3]

    caselist.append({
      'name': name,
      'url': url,
      'docket': docket,
      'volume': volume,
      'date': datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
      })

  return caselist


def main():
  url_base = JUSTIA_YEAR_URL
  start_year = START_YEAR
  end_year = END_YEAR
  years = list(range(start_year, end_year+1))
  output_file = CASELIST
  data_dir = DATA_DIR

  urls = [url_base + str(y) + '.html' for y in years]

  with ProcessPoolExecutor() as executor:
    caselist = list(executor.map(process_page, urls))

  caselist = [item for sublist in caselist for item in sublist]

  if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    print(f"Directory '{data_dir}' created.")

  with open (output_file, 'w') as json_file:
    json.dump(caselist, json_file, indent=2)

  print(f'Data saved to {output_file}')


if __name__ == "__main__":
  main()
