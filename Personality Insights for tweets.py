import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


CLIENT_SECRETS_FILE = "client_secret.json"
with open(CLIENT_SECRETS_FILE) as json_data:
    d = json.load(json_data)
    twitter_consumer_key = d['ckey']
    twitter_consumer_secret = d['csecret']
    twitter_access_token = d['atoken']
    twitter_access_secret = d['asecret']

WATSON_SECRET_FILE = "watson_secret .json"
with open(WATSON_SECRET_FILE) as json_data:
    d = json.load(json_data)
    pi_username = d['pi_username']
    pi_password = d['pi_password']


twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret,
                          access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)


def analyze(handle):
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
    text = b''
    for status in statuses:
        if (status.lang == 'en'):  # English tweets
            if (status.lang == 'en'):
                text += status.text.encode('UTF-8')
    personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
    pi_result = personality_insights.profile(text)
    return pi_result


def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                            data[c3['id']] = c3['percentage']
    return data


def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            compared_data[keys] = abs(dict1[keys] - dict2[keys])
    return compared_data


user_handle = "@billclinton"
celebrity_handle = "@realDonaldTrump"

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)
user = flatten(user_result)
celebrity = flatten(celebrity_result)
compared_results = compare(user, celebrity)
sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))


for keys, value in sorted_result:
    print(keys),
    print(user[keys]),
    print('->'),
    print(celebrity[keys]),
    print('->'),
    print(compared_results[keys])

