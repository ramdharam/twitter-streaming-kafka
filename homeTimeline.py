import tweepy
import json
import os
import sys

cwd = os.getcwd()
#print (cwd)
file_path = os.path.join(cwd, 'creds.json')
#print (file_path)


with open(file_path) as json_data:
    d = json.load(json_data)

consumer_key=d['consumer_key']
consumer_secret=d['consumer_secret']
access_token=d['access_token']
access_token_secret=d['access_token_secret']

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    #print(tweet)
    sys.stdout.write(tweet.text)
