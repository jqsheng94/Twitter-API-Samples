from TwitterAPI import TwitterAPI, TwitterRestPager
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

SEARCH_TERM = 'trump'


pager = TwitterRestPager(api, 'search/tweets', {'q': SEARCH_TERM})

for item in pager.get_iterator():
    print(item['text'] if 'text' in item else item)
