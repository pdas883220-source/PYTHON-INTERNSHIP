# Day 41 - Python Web Scraping

import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://quotes.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check response
if response.status_code == 200:

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes
    quotes = soup.find_all("span", class_="text")

    print("Quotes from Website:\n")

    for i, quote in enumerate(quotes, start=1):
        print(i, quote.text)

else:
    print("Unable to access website.")