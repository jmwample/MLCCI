#!/bin/python
"""--------------------------------------------------------------------------
@author     Jack wampler
@file       parse.py
@purpose    Test out the twitter Streaming API 

@future     Create a running sentiment analysis app that will measure 
            public sentiment of a topic based on key word values.
@reference  http://adilmoujahid.com/posts/2014/07/twitter-analytics/

--------------------------------------------------------------------------"""
import config as cfg        # Stored credentials and urls
import json
import matplotlib.pyplot as plt 
import pandas as pd
import re



def getData(filepath):
    tweets_d = []                       # data
    tweets_f = open(filepath, 'r')      # file
    
    for line in tweets_f:
        if line == '\n':
            continue
        try:
            twt = json.loads(line )
            tweets_d.append(twt)
            print( [ x['text'] for x in twt['entities']['hashtags']] )
        except: 
            continue

    tweets_f.close()

    return tweets_d


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

def plotCountries(tweets):
    tweets_by_country = tweets['country'].value_counts()

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Countries', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

    plt.show()


def plotLanguages(tweets): 
    tweets_by_lang = tweets['lang'].value_counts()

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
    tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

    plt.show()

def main():
    tweets_dp = "./twitter_data_l.txt"    # datapath
    tweets_d  = getData(tweets_dp)      # data
    print( len(tweets_d) )
    tweets = pd.DataFrame()

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_d)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_d)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_d)
    tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
    tweets_relevant = tweets[tweets['relevant'] == True]
    tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

    # Print the links extracted from the tweets by the regex
    print tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link']
    print tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link']
    print tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link']


    plotCountries(tweets)


if __name__ == "__main__":
    main()
