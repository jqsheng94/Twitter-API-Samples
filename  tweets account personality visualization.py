import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
import matplotlib.pyplot as plt
import matplotlib.cm as cm, matplotlib.font_manager


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



user_handle = "@HillaryClinton"
celebrity_handle = "@realDonaldTrump"

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)
user = flatten(user_result)
celebrity = flatten(celebrity_result)



def gbplot_pie(user, title, cm_name='Pastel1', autopct='%1.1f%%', labeldistance=1.05, shadow=True, startangle=90, edgecolor='w', width=8, height=8, grouping_threshold=None, grouping_label=None):  # what the label the grouped wedge
    fractions = [i for i in user.values()]
    labels = [i for i in user.keys()]
    if not grouping_threshold == None:
        if grouping_label == None:
            grouping_label = 'Others'
        row_mask = fractions > grouping_threshold
        meets_threshold = fractions[row_mask]
        all_others = pd.Series(fractions[~row_mask].sum())
        all_others.index = [grouping_label]
        fractions = meets_threshold.append(all_others)
        labels = fractions.index
    color_map = cm.get_cmap(cm_name)
    num_of_colors = len(labels)
    colors = color_map([float(x /num_of_colors) for x in range(num_of_colors)])
    fig, ax = plt.subplots(figsize=[width, height])
    plt.title(title)
    wedges = ax.pie(fractions, labels=labels, labeldistance=labeldistance, autopct=autopct, colors=colors, shadow=shadow, startangle=startangle)
    for wedge in wedges[0]:
        wedge.set_edgecolor(edgecolor)
    plt.savefig("./Output/" + title + ".png")
    plt.close('all')


gbplot_pie(user, user_handle)
gbplot_pie(celebrity, celebrity_handle)
