"""
Author: Yashkir Ramsamy
Contact: me@yashkir.co.za
Date: 2020/07/13

Purpose:
"""

import requests
from bs4 import BeautifulSoup

DATA_SOURCE = "https://www.worldometers.info/coronavirus/country/south-africa/"
stats = []

def parse():
    print("Getting web content")
    web_page = requests.get(DATA_SOURCE).content
    soup = BeautifulSoup(web_page, "html.parser")
    print("Parsing web content")
    for div in soup.find_all('div', class_='maincounter-number'):
        stats.append(div.span.text)

def getCases():
    return stats[0]

def getDeaths():
    return stats[1]

def getRecovered():
    return stats[2]

