import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

@anvil.server.callable
def start_scraping(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example scraping logic (can be extended)
        title = soup.title.string if soup.title else "No Title"
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        # Save to data table (or any other processing)
        app_tables.scraped_data.add_row(url=url, title=title, content=" ".join(paragraphs))

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
