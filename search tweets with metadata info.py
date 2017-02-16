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

r = api.request('search/tweets', {'q': SEARCH_TERM, 'count' : 100})

for item in r:
    if 'text' in item and 'user' in item:
        location = item['user']['location']
        tweet = item['text']
        lang = item['lang']
        metadata = item['metadata']
        tweetLanguage = metadata['iso_language_code']
        username = item['user']['name']
        if len(location) > 1:
            print (location,tweetLanguage, lang, tweet, username)






