#!/bin/python 
"""

"""
import config as cfg
from collections import deque
import json
from matplotlib import pyplot as plt
import re
import sys
from textblob import TextBlob
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



#Variables that contains the user credentials to access Twitter API 
access_token = cfg.api['api_at']
access_token_secret = cfg.api['api_at_secret']
consumer_key = cfg.api['api_consumer_key']
consumer_secret = cfg.api['api_consumer_secret']


#This is a basic listener that just prints received tweets to stdout.
class myStdOutListener(StreamListener):


    def __init__(self):
        StreamListener.__init__(self)
        self.tweets_1k = deque([{"pol":0}]*10)
        self.tweets_10k = deque([{"pol":0}]*100)
        #self.plot_sentiment()
        l = len(self.tweets_1k)
        self.X = range(0,l)
        self.Y = [ self.tweets_1k[x]["pol"] for x in self.X ]

        plt.ion()
        self.graph = plt.plot(self.X,self.Y)[0]



    def push_tweet(self, tweet):
        self.check_lengths()
        # sys.stdout.write(".")
        # sys.stdout.flush()
        self.tweets_1k.append(tweet)
        self.tweets_10k.append(tweet)
        self.Y = [ self.tweets_1k[x]["pol"] for x in self.X ]
        self.graph.set_ydata(self.Y)
        plt.ylim((-1.5,1.5))
        plt.draw()
        plt.pause(1)
        return True


    def check_lengths(self):
        if len(self.tweets_1k) >= 10:
            self.tweets_1k.popleft()
        if len(self.tweets_10k) >= 100:
            self.tweets_10k.popleft()


    def on_status(self, status):
        if status.retweeted:
            return
        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color

        #print(text)

        blob = TextBlob(text)
        sentiment = blob.sentiment 

        #print (sentiment.polarity, sentiment.subjectivity)
        tweet ={"text":text,"loc":loc,
                "subj":sentiment.subjectivity,
                "pol":sentiment.polarity
        } 
        # print tweet["pol"]

        self.push_tweet(tweet)


    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            print status
            return True





if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = myStdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
                                                                    
    #This line filter Twitter Streams to capture data by keywords relevant to cryptocurrencies
    stream.filter(track=['bitcoin', 'ethereum', 'btc-usd'])
    l.plot_sentiment()




"""
import io

output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
"""
