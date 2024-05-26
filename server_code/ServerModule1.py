import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

@anvil.server.callable
def test_server():
    return "Server is running"
  
def start_scraping(url):
    try:
        print(f"Starting scrape for URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        print("HTTP request successful")
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Parsed HTML")

        title = soup.title.string if soup.title else "No Title"
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        app_tables.scraped_data.add_row(url=url, title=title, content=" ".join(paragraphs))

        print("Data saved successfully")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
