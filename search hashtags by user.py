import yaml
import twitter
import json


CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)
    ckey = d['ckey']
    csecret = d['csecret']
    atoken = d['atoken']
    asecret = d['asecret']


api = twitter.Api(ckey, csecret, atoken, asecret)
user = "realDonaldTrump"
statuses = api.GetUserTimeline(screen_name=user, count=500, include_rts=False)

Hashtags = []
for i in statuses:
    i = json.dumps(i._json)
    i = yaml.load(i)
    hashtags = i['entities']['hashtags']
    if len(hashtags) >0 :
        text = hashtags[0]['text']
        Hashtags.append(text)

print(Hashtags)









