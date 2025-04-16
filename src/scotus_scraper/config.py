import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATA_DIR = os.path.join(BASE_DIR, 'data')
JUSTIA_CASE_PAGES_DIR = os.path.join(DATA_DIR, 'justia_case_pages')

AMICUS_BRIEFS_LIST = os.path.join(DATA_DIR, 'amicus_briefs_list.json')
AMICUS_BRIEFS_TEXT = os.path.join(DATA_DIR, 'amicus_briefs_text.json')
FILINGS = os.path.join(DATA_DIR, 'filings.json')
CASE_MEDIA = os.path.join(DATA_DIR, 'case_media.json')
CASELIST = os.path.join(DATA_DIR, 'caselist.json')
JUSTIA_CASE_PAGES_PARSED = os.path.join(DATA_DIR, 'justia_case_pages_parsed.json')
OPINIONS_TEXT = os.path.join(DATA_DIR, 'opinions_text.json')
SYLLABUS_TEXT = os.path.join(DATA_DIR, 'syllabus_text.json')
CASE_MEDIA = os.path.join(DATA_DIR, 'case_media.json')
CASE_FILINGS = os.path.join(DATA_DIR, 'filings.json')

JUSTIA_URL = 'https://supreme.justia.com'
JUSTIA_YEAR_URL = JUSTIA_URL + '/cases/federal/us/year/'

START_YEAR = 2020
END_YEAR = 2024
