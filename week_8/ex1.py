import requests
import cloudscraper

from bs4 import BeautifulSoup

artist_names = []

url = f'https://www.moma.org/artists/?exhibition_id=5224'


scraper = cloudscraper.create_scraper()
page = scraper.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


print(soup.findAll('h3', 'span', class_='layout/block'))


print(artist_names)
