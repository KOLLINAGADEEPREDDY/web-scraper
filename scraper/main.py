import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else "No title"
    except Exception as e:
        return f"Error: {e}"