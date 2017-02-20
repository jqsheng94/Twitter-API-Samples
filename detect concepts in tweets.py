from TwitterAPI import TwitterAPI, TwitterRestPager
import json
import sys
sys.path.append('./Alchemy')
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

SEARCH_TERM = 'Election'

r = api.request('search/tweets', {'q': SEARCH_TERM, 'count' : 10})

for item in r:
    if 'text' in item:
        tweet = item['text']
        username = item['user']['name']
        response = alchemyapi.concepts('text', tweet)
        if response['status'] == 'OK':
            for concept in response['concepts']:
                results = json.dumps(response, indent=4)
                text = concept['text']
                relevance = concept['relevance']
        else:
            text = 'None'
            relevance = 0
            print('Error in concept tagging call: ', response['statusInfo'])
    print(text, relevance, tweet)






