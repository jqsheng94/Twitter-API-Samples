
import twitter
import json


CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)
    ckey = d['ckey']
    csecret = d['csecret']
    atoken = d['atoken']
    asecret = d['asecret']


# Create an Api instance.
api = twitter.Api(consumer_key=ckey,
                  consumer_secret=csecret,
                  access_token_key=atoken,
                  access_token_secret=asecret)

Following = api.GetFriends()

print([u.screen_name for u in Following])