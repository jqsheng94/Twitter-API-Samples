# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:30:56 2017

@author: jiaqi
"""


import yaml
import twitter
import json
import re
import matplotlib
matplotlib.style.use('ggplot')



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
    
    publishTime = []
    
    for i in statuses:
        i = json.dumps(i._json)
        i = yaml.load(i)
        source = i['source']
        source = re.findall('http://twitter.com/download/(.*)" rel="nofollow">Twitter', source)[0]
        time = i['created_at']
        publishTime.append(time)
    Last = publishTime[0], 
    First = publishTime[-1]
    return Last, First
                        
#    return publishTime    

testUser = "realDonaldTrump"    
print(findTweetsStats(testUser))
#results = list(findTweetsStats(testUser))







