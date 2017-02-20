from TwitterAPI import TwitterAPI, TwitterRestPager
import json
import sys
sys.path.append('./Alchemy')  # path to alchemyapi_python's folder to make the import work
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()


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

SEARCH_TERM = 'donald trump'

r = api.request('search/tweets', {'q': SEARCH_TERM, 'count' : 10})

for item in r:
    if 'text' in item and 'user' in item:
        tweet = item['text']
        username = item['user']['name']
        response = alchemyapi.sentiment('html', tweet)
        if response['status'] == 'OK':
            results = json.dumps(response, indent=4)
            type = response['docSentiment']['type']
            if 'score' in response['docSentiment']:
                score = response['docSentiment']['score']
            else:
                score = 0
        else:
            print('Error in sentiment analysis call: ', response['statusInfo'])
        print(username)
        print('=================Output========================')
        print(score)
        print(type)
        print(tweet)






