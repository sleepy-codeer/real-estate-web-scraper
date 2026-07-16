import requests as rq 
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def extract_text(parent, tag, class_name): 
    element = parent.find(tag, class_=class_name)
    return element.text.strip() if element else "N/A"

print("Starting Real EstateBy Cra developers LLP Pipeline...")

DIRECTORY = []
page = 1
max_pages = 54 

session = rq.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

while page <= max_pages:
    print(f"Scraping Page {page}...")
    
    if page == 1:
        url = "https://www.realestateindia.com/delhi-property/new-projects.htm"
    else:
        url = f"https://www.realestateindia.com/delhi-property/new-projects-{page}.htm"

    response = session.get(url, timeout=10)

    if response.status_code != 200: 
        print(f"Hit a wall at page {page} or got blocked. Stopping loop.")
        break

    soup = bs(response.content, 'html.parser')
    property_cards = soup.find_all('div', class_="spc-info")

    if not property_cards:
        print("No more properties found. Extraction complete.")
        break

    for card in property_cards: 
        property_title = extract_text(card, 'strong', 'spcf-val sc')
        property_price = extract_text(card, 'div', 'spc-price')
        builder = extract_text(card, 'h2', 'spc-title')
        property_address = extract_text(card, 'p', 'spc-location')

        DIRECTORY.append({
            "Title": property_title, 
            "Price": property_price,
            "Builder": builder,
            "Location": property_address.split('\n')[0]
        })
    
    time.sleep(2)
    page += 1

print(f"\nSuccessfully extracted {len(DIRECTORY)} properties!")
table = pd.DataFrame(DIRECTORY)
table.to_csv('real_estate_delhi.csv', index=False)
print("Data saved to real_estate_delhi.csv")
