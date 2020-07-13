"""
Author: Yashkir Ramsamy
Contact: me@yashkir.co.za
Date: 2020/07/13

Purpose: Bot which tweets corona virus stat updates
"""

import tweepy
import webParser
import operator
from config import *
from datetime import datetime
from pytz import timezone

# emojis
chart_increasing = "\U0001F4C8"  # for cases
wilting_rose = "\U0001F940"  # for deaths
sneezing_face = "\U0001F927"  # for active cases
sick_emoji = "\U0001F912"  # for active cases
raising_hands = "\U0001F64C"  # for recoveries

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_account = tweepy.API(auth)


# params: cases, deaths, recoveries, active_cases
def tweet(c, d, r, a_c):
    cases = "{:,}".format(c)
    deaths = "{:,}".format(d)
    recoveries = "{:,}".format(r)
    active_cases = "{:,}".format(a_c)
    south_africa = timezone('Africa/Johannesburg')
    sa_time = datetime.now(south_africa)
    date = sa_time.strftime('%d/%m')

    status_text = \
        "South Africa's COVID-19 STATS - {date}" \
        "\n\n{chart_increasing} Cases: {cases}" \
        "\n{wilting_rose} Deaths: {deaths}" \
        "\n{raising_hands} Recoveries: {recoveries}" \
        "\n{sneezing_face} Active Cases: {active_cases}" \
        "\n\n #CoronaVirusSA #COVID19 {pop_tag}" \
            .format(cases=cases, deaths=deaths, recoveries=recoveries, active_cases=active_cases,
                    chart_increasing=chart_increasing, wilting_rose=wilting_rose, sneezing_face=sick_emoji,
                    raising_hands=raising_hands, date=date, pop_tag=getTrendingTag())
    print("Tweeting")
    twitter_account.update_status(status_text)
    print("Tweeted!")


def getTrendingTag():
    trends_dict = twitter_account.trends_place(23424942)
    trends = trends_dict[0]
    trends_dict_sum = {}
    for dict in trends['trends']:
        if dict['tweet_volume'] == None:
            dict['tweet_volume'] = 0
        trends_dict_sum[dict['name']] = dict['tweet_volume']
    print("Finding most popular tag from: ", trends_dict_sum)
    return max(trends_dict_sum.items(), key=operator.itemgetter(1))[0]


# Run Bot
def main():
    stats = webParser.getNationalStats()
    cases = stats[0]
    deaths = stats[1]
    recoveries = stats[2]
    active_cases = stats[0] - stats[2]
    tweet(cases, deaths, recoveries, active_cases)


if __name__ == "__main__":
    main()
