"""
Author: Yashkir Ramsamy
Contact: me@yashkir.co.za
Date: 2020/07/13

Purpose: Bot which tweets corona virus stat updates
"""

import tweepy
import webParser
from config import *

# emojis
chart_increasing = "\U0001F4C8"  # for cases
wilting_rose = "\U0001F940"  # for deaths
sneezing_face = "\U0001F927"  # for active cases
sick_emoji = "\U0001F912"  # for active cases
raising_hands = "\U0001F64C"  # for recoveries

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_account = tweepy.API(auth)


def tweet(cases, deaths, recoveries, active_cases):
    status_text = \
        "{chart_increasing} Cases: {cases}" \
        "\n{wilting_rose} Deaths: {deaths}" \
        "\n{raising_hands} Recoveries: {recoveries}" \
        "\n{sneezing_face} Active Cases: {active_cases}" \
            .format(cases=cases, deaths=deaths, recoveries=recoveries, active_cases=active_cases,
                    chart_increasing=chart_increasing, wilting_rose=wilting_rose, sneezing_face=sick_emoji,
                    raising_hands=raising_hands)
    print("Tweeting")
    twitter_account.update_status(status_text)
    print("Tweeted!")




# Run Bot
def main():
    stats = webParser.getStats()
    cases = stats[0]
    deaths = stats[1]
    recoveries = stats[2]
    active_cases = stats[0] - stats[2]
    tweet(cases, deaths, recoveries, active_cases)


if __name__ == "__main__":
    main()
