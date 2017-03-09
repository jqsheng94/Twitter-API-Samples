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



def findTweetsStats(username):
    api = twitter.Api(ckey, csecret, atoken, asecret)
    user = username
    statuses = api.GetUserTimeline(screen_name=user, count=500, include_rts=False)

    DirectFavoriteCount = 0
    DirectReteetedCount = 0
    DirectCount = 0
    
    
    for i in statuses:
        i = json.dumps(i._json)
        i = yaml.load(i)
        favorite_count = i['favorite_count']
        text = i['text']
        retweeted = i['retweeted']
        language = i['lang']
        retweet_count = i['retweet_count']
        if retweeted is False:
            DirectFavoriteCount += favorite_count
            DirectReteetedCount += retweet_count
            DirectCount += 1
        return DirectFavoriteCount/DirectCount, DirectReteetedCount/DirectCount
 
     
print(findTweetsStats("realDonaldTrump"))
print(findTweetsStats("HilaryClinton"))










