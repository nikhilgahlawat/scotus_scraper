import os
from concurrent.futures import ProcessPoolExecutor
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
from scotus_scraper.config import JUSTIA_CASE_PAGES_DIR, SYLLABUS_TEXT, OPINIONS_TEXT, CASE_MEDIA, CASE_FILINGS

def parse_data(soup):
  case = {
    'docket': None,
    'syllabus': None,
    'opinion_labels': None,
    'opinions': None,
    'media': [],
    'filings': []
  }

  docket = soup.find('div', id='top').find('div', class_='flex-col width-20 reset-width-below-tablet item').get_text().strip().split('\n')[1]
  syllabus = soup.find('div', class_='block syllabus')
  opinion_labels = soup.find('div', id='tab-opinion')
  opinions = soup.find_all('div', class_='-display-inline-block text-left')
  media = soup.find('div', id='tab-audio-and-media')
  filings = soup.find('div', id='tab-briefs-and-filings')

  if docket:
    case['docket'] = docket

  if syllabus:
    case['syllabus'] = re.sub(r'\s+', ' ', syllabus.get_text()).strip()

  if opinion_labels:
    opinion_labels = opinion_labels.find_all('li')
    case['opinion_labels'] = [re.sub(r'\s+', ' ', ol.get_text()).strip() for ol in opinion_labels]
  
  if opinions:
    case['opinions'] = [re.sub(r'\s+', ' ', opinion.get_text()).strip() for opinion in opinions]
    
  if media:
    items = media.find_all('tr')
    for item in items:
      # full_text = item.text.strip()
      text = item.find('a').text
      url = item.find('a')['href']
      
      case['media'].append({
        'text': text,
        'url': url
      })

  if filings:
    items = filings.find_all('tr')
    for item in items:
      cols = item.find_all('td')
      date = datetime.strptime(cols[0].text, '%b %d, %Y').strftime('%Y-%m-%d')
      text = cols[1].text.strip()

      links = cols[1].find_all('a')
      docs = [{'name': link.text.strip(), 'url': link['href']} for link in links]
      
      case['filings'].append({
        'date': date,
        'text': text,
        'docs': docs
      })

  return case

def process_file(file_path):
  with open(file_path, 'r') as file:
    content = file.read()
  soup = BeautifulSoup(content, 'html.parser')
  data = parse_data(soup)
  return data

def write_json(data, filename):
  with open(filename, 'w') as json_file:
    json.dump(data, json_file, indent=2)

def main():
  input_dir = JUSTIA_CASE_PAGES_DIR
  syllabus_file = SYLLABUS_TEXT
  opinions_file = OPINIONS_TEXT
  media_file = CASE_MEDIA
  filings_file = CASE_FILINGS
  opinion_label_pattern = r'^(.*?)(?: \((.*?)\))?$'

  files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith('.html')]

  with ProcessPoolExecutor() as executor:
    cases = list(executor.map(process_file, files))

  syllabi = [{'docket': case['docket'], 'syllabus': case['syllabus']} for case in cases if case['syllabus']]
  write_json(syllabi, syllabus_file)

  opinions = []
  for case in cases:
    if case['opinions']:
      for label, text in zip(case['opinion_labels'], case['opinions']):

        match = re.match(opinion_label_pattern, label)
        if match:
          opinion_type = match.group(1)
          author = match.group(2) if match.group(2) else None

        opinions.append({
          'docket': case['docket'],
          # 'label': label,
          'type': opinion_type,
          'author': author,
          'text': text
          })
  write_json(opinions, opinions_file)

  media = [{'docket': case['docket'], 'media': case['media']} for case in cases if case['media']]
  write_json(media, media_file)

  filings = [{'docket': case['docket'], 'filings': case['filings']} for case in cases if case['filings']]
  write_json(filings, filings_file)


if __name__ == "__main__":
  main()
