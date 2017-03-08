import os
import json
import twitter

CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)
    ckey = d['ckey']
    csecret = d['csecret']
    atoken = d['atoken']
    asecret = d['asecret']

USERS = ['@twitter',
         '@support']

LANGUAGES = ['en']

api = twitter.Api(consumer_key=ckey,
                  consumer_secret=csecret,
                  access_token_key=atoken,
                  access_token_secret=asecret)

def main():
    with open('./Output/UserTrack.txt', 'a') as f:

        for line in api.GetStreamFilter(track=USERS, languages=LANGUAGES):
            f.write(json.dumps(line))
            f.write('\n')

if __name__ == '__main__':
    main()

