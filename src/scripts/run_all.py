import scotus_scraper.config
from scotus_scraper import justia_case_urls, justia_case_pages_html, justia_case_pages_parse

def main():
  justia_case_urls.main()
  justia_case_pages_html.main()
  justia_case_pages_parse.main()

if __name__ == "__main__":
  main()
