from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import os


CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)
    ckey = d['ckey']
    csecret = d['csecret']
    atoken = d['atoken']
    asecret = d['asecret']

class listener(StreamListener):
    def __init__(self):
        self.tweet_data = []
    def on_data(self, data):
        if len(self.tweet_data) <= 10:
            print(len(self.tweet_data))
            try:
                self.tweet_data.append(data)
                print(self.tweet_data)
                return self.tweet_data
            except BaseException:
                print('failed ondata,', str(BaseException))
                pass
        else:
            print(self.tweet_data)
    def on_error(self, status):
        print(status)

start_time = time.time()
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

def getLocationTweets(location):
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=['trump'], locations= location)

NewYort =  getLocationTweets ([-74,40,-73,41])
LosAngeles = getLocationTweets ([-118,34])
Chicago =  getLocationTweets ([-87,41])
Seattle = getLocationTweets ([-112,47])
Phoenix = getLocationTweets ([-112,33])
SanDiego = getLocationTweets ([-117,32])
SanFrancisco =  getLocationTweets([-122.75,36.8,-121.75,37.8])
Austin = getLocationTweets ([-97,30])
Detroit = getLocationTweets ([-83,42])
Boston = getLocationTweets ([-71,42])



