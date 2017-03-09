import yaml
import twitter
import json
import re


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
    statuses = api.GetUserTimeline(screen_name=user, count=100, include_rts=False)
    
    iphoneFavoritecount = 0
    iphoneRetweetcount = 0
    iphoneTweetcount = 0
    androidFavoritecount = 0
    androidRetweetcount = 0
    androidTweetcount = 0
    
    for i in statuses:
        i = json.dumps(i._json)
        i = yaml.load(i)
        source = i['source']
        source = re.findall('http://twitter.com/download/(.*)" rel="nofollow">Twitter', source)[0]
        favorite_count = i['favorite_count']
        retweet_count = i['retweet_count']
        if source == 'iphone':
            iphoneTweetcount += 1
            iphoneFavoritecount += favorite_count 
            iphoneRetweetcount += retweet_count
        if source == 'android':
            androidTweetcount += 1
            androidFavoritecount += favorite_count 
            androidRetweetcount += retweet_count
               
    return iphoneFavoritecount/iphoneTweetcount, iphoneRetweetcount/iphoneTweetcount, androidFavoritecount/androidTweetcount, androidRetweetcount/androidTweetcount    
     
     
print(list(findTweetsStats("realDonaldTrump")))