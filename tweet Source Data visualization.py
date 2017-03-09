# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:18:01 2017

@author: jiaqi
"""

import yaml
import twitter
import json
import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np



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
     
    
testUser = "realDonaldTrump"    
results = list(findTweetsStats(testUser))
AvgIphoneFavorite = results[0]
AveIphoneRetweet = results[1]
AvgAndroidFavorit = results[2]
AvgAndroidRetweet = results[3]
n=2
fig, ax = plt.subplots(2)
bar_width = 0.4  # default: 0.8
bar_locations = np.arange(n)
data1 = np.array([float(AvgIphoneFavorite), float(AvgAndroidFavorit)])
data2 = np.array([AveIphoneRetweet, AvgAndroidRetweet])
ax[0].bar(bar_locations, data1, bar_width)
ax[0].bar(bar_locations - bar_width,data2,bar_width,color='r')

ax[1].bar(bar_locations, data1, bar_width)
ax[1].bar(bar_locations - (bar_width / 2), data2, bar_width, color='r')
plt.savefig("./Output/Source" + testUser + ".png")
plt.close('all')






