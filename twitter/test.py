#!/bin/python 
"""

"""
import config as cfg
import io
import json
import re
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
class StdOutListener(StreamListener):


    def on_status(self, status):
        #if status.retweeted_status:
        #    return
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

        print(text)

        blob = TextBlob(text)
        sentiment = blob.sentiment 

        print (sentiment.polarity, sentiment.subjectivity)
    

    """def on_data(self, data):
        #print data
        try:
            tweet = json.loads(data)
            print(tweet['text'], [ x['text'] for x in tweet['entities']['hashtags'] ])
        except:
            return False
        return True
        """

    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            print status
            return True





if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
                                                                    
    #This line filter Twitter Streams to capture data by keywords relevant to cryptocurrencies
    stream.filter(track=['bitcoin', 'ethereum', 'btc-usd'])




"""
mport io

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
