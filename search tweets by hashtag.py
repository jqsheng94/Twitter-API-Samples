
import json
from twitter import Twitter, OAuth

CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)
    ckey = d['ckey']
    csecret = d['csecret']
    atoken = d['atoken']
    asecret = d['asecret']



oauth = OAuth(atoken, asecret, ckey, csecret)
t = Twitter(auth=oauth)
query = t.search.tweets(q='%23cat')  # %23 is URL encoded form of #

for s in query['statuses']:
    print(s['created_at'], s['text'], '\n')