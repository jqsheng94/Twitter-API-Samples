from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)
    ckey = d['ckey']
    csecret = d['csecret']
    atoken = d['atoken']
    asecret = d['asecret']

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
twitterStream.filter(track = ['election'], locations =[-122.75,36.8,-121.75,37.8]) #locations can be change to any place with comma-separated list of longitude and latitude in pairs
# [-122.75,36.8,-121.75,37.8]	San Francisco
# [-74,40,-73,41]	New York City
# [-122.75,36.8,-121.75,37.8,-74,40,-73,41]	San Francisco OR New York City
