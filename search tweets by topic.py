from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey = "XXX"
csecret = "XXXX"
atoken = "XXXXXX"
asecret = "XXXXXXX"


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        print(username, tweet)
        return True
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["election"]) #track can be change to any topic
