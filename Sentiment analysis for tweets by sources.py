# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:18:01 2017

@author: jiaqi
"""

import yaml
import twitter
import json
import re
import matplotlib
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



def findTweetsStats(username):
    api = twitter.Api(ckey, csecret, atoken, asecret)
    user = username
    statuses = api.GetUserTimeline(screen_name=user, count=100, include_rts=False)
    
    iphoneTweetcount = 0
    iphoneSentScore = 0
    androidTweetcount = 0
    androidSentScore = 0
    
    
    for i in statuses:
        i = json.dumps(i._json)
        i = yaml.load(i)
        source = i['source']
        source = re.findall('http://twitter.com/download/(.*)" rel="nofollow">Twitter', source)[0]
        text = i['text']
        response = alchemyapi.sentiment('html', text)
        if response['status'] == 'OK':
            response = json.dumps(response, indent=4)
            if "score" in response['docSentiment']:
                score = float(response['docSentiment']['score'])
            else:
                score = 0
        else:
            score = 0
        if source == 'iphone':
            iphoneTweetcount += 1
            iphoneSentScore += score
        if source == 'android':
            androidTweetcount += 1
            androidSentScore += score
               
    return iphoneSentScore/iphoneTweetcount,  androidSentScore/androidTweetcount   
     
    
testUser = "realDonaldTrump"    
results = list(findTweetsStats(testUser))
AvgIphoneSentScore = results[0]
AvgAndroidSentScore = results[1]







