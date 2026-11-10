Delhi Real Estate Project Scraper
Overview

This Python program scrapes new real estate project listings in Delhi from RealEstateIndia. It extracts property details and saves them into a CSV file for further analysis.

Features
Scrapes up to 54 pages of property listings.
Extracts property title, price, builder, and location.
Uses BeautifulSoup to parse website content.
Uses Requests to fetch webpage data.
Saves extracted data into real_estate_delhi.csv.
Requirements

Install the required Python libraries:

bash
pip install requests beautifulsoup4 pandas

How to Run
Save the script as scraper.py.
Install the required dependencies.
Run the program:
bash
python scraper.py

The extracted data will be saved as real_estate_delhi.csv in the current directory.
Output

The CSV file contains the following columns:

Title: Property project name.
Price: Listed property price.
Builder: Developer or builder name.
Location: Property location.
Note

The scraper stops if a page cannot be accessed or no more property listings are found. Website structure changes may require updates to the scraping code. Please respect the website's terms of use and scraping policies.
