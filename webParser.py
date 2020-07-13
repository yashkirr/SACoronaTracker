"""
Author: Yashkir Ramsamy
Contact: me@yashkir.co.za
Date: 2020/07/13

Purpose:
"""

import requests
from bs4 import BeautifulSoup

DATA_SOURCE = "https://www.worldometers.info/coronavirus/country/south-africa/"
stats = []  # in case there's a need to implement more


def parse():
    print("Getting web content")
    web_page = requests.get(DATA_SOURCE).content
    soup = BeautifulSoup(web_page, "html.parser")
    print("Parsing web content")
    for div in soup.find_all('div', class_='maincounter-number'):
        stat = div.span.text
        stats.append(int(stat.replace(',', '')))
# returns list where:
#   [0]: Cases
#   [1]: Deaths
#   [2]: Recoveries
def getStats():
    parse()
    return stats

if __name__ == "__main__":
    print(getStats())