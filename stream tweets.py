from TwitterAPI import TwitterAPI
import json

CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)

    ckey = d['ckey']
    csecret = d['csecret']
    atoken = d['atoken']
    asecret = d['asecret']

api = TwitterAPI(ckey,
                 csecret,
                 atoken,
                 asecret)

TRACK_TERM = 'trump'

r = api.request('statuses/filter', {'track': TRACK_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)
