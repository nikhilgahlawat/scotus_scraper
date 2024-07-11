import json
import re
from scotus_scraper.config import JUSTIA_CASE_PAGES_PARSED, AMICUS_BRIEFS_LIST


def contains_amicus(item):
  pattern = r'^amicus|^amici|^brief'
  return bool(re.search(pattern, item.lower()))

def main(input_file, output_file):
  with open(input_file, 'r') as json_file:
    cases = json.load(json_file)

  amicus_briefs = []

  for case in cases:
    for item in case['filings']:
      urls = [doc['url'] for doc in item['docs'] if doc['name'] == 'Main Document']
  
      if contains_amicus(item['text']) and len(urls)>0:
        amicus_briefs.append({
          'docket': case['docket'],
          'date': item['date'],
          'label': item['text'],
          'url': urls[0]
        })

  with open(output_file, 'w') as json_file:
    json.dump(amicus_briefs, json_file, indent=2)

  print(f"Processed files and saved to {output_file}")

if __name__ == "__main__":
  input_file = JUSTIA_CASE_PAGES_PARSED
  output_file = AMICUS_BRIEFS_LIST
  
  main(input_file, output_file)
