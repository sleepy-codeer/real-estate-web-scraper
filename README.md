# Delhi Real Estate Project Scraper

## Overview

This Python program scrapes new real estate project listings in Delhi from RealEstateIndia. It extracts important property details and saves the collected data into a CSV file for further analysis.

## Features

- Scrapes up to 54 pages of property listings.
- Extracts property title, price, builder, and location.
- Uses BeautifulSoup to parse website content.
- Uses Requests to fetch webpage data.
- Saves extracted data into `real_estate_delhi.csv`.
- Stops scraping if a page cannot be accessed or no more property listings are found.

## Requirements

Make sure Python is installed on your system.

Install the required Python libraries using:

```bash
pip install requests beautifulsoup4 pandas
