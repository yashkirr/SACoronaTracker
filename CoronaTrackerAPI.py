"""
Author: Yashkir Ramsamy
Contact: me@yashkir.co.za
Date: 2020/07/14

Purpose: API used for getting data from coronatracker.com
"""

import requests


def getNationalStats():
    result = requests.get("http://api.coronatracker.com/v3/stats/worldometer/country", {"countryCode": "ZA"})
    response = result.json()[0]
    stats = [response["totalConfirmed"], response["totalDeaths"], response["totalRecovered"]]
    return stats

if __name__ == "__main__":
    print(getNationalStats())
