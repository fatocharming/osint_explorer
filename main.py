import requests
from bs4 import BeautifulSoup
import json

def fetch_ip_info(ip_address):
    """Fetch IP information from an online API."""
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    return response.json()

def scrape_website(url):
    """Scrape a website and extract titles and paragraphs."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [title.get_text() for title in soup.find_all('h1')]
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    return titles, paragraphs

def main():
    # Example IP address for OSINT
    ip_address = "8.8.8.8"  # Google Public DNS
    ip_info = fetch_ip_info(ip_address)
    print("IP Information:")
    print(json.dumps(ip_info, indent=2))

    # Example website for scraping
    website_url = "https://example.com"
    titles, paragraphs = scrape_website(website_url)
    print("\nWebsite Titles:")
    for title in titles:
        print(f"- {title}")
    
    print("\nWebsite Paragraphs:")
    for paragraph in paragraphs:
        print(f"- {paragraph[:100]}...")  # Print first 100 chars

if __name__ == "__main__":
    main()