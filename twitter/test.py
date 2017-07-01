#!/bin/python 
"""


"""
import config as cfg
import json
import re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



#Variables that contains the user credentials to access Twitter API 
access_token = cfg.api['api_at']
access_token_secret = cfg.api['api_at_secret']
consumer_key = cfg.api['api_consumer_key']
consumer_secret = cfg.api['api_consumer_secret']


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

        def on_data(self, data):
            #print data
            try:
                tweet = json.loads(data)
                print(tweet['text'], [ x['text'] for x in tweet['entities']['hashtags'] ])
            except:
                return False
            return True

        def on_error(self, status):
            print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
                                                                    
    #This line filter Twitter Streams to capture data by keywords relevant to cryptocurrencies
    stream.filter(track=['bitcoin', 'ethereum', 'btc-usd'])
