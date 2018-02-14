import tweepy
import json
import os

cwd = os.getcwd()
print (cwd)
file_path = os.path.join(cwd, 'creds.json')
print (file_path)


with open(file_path) as json_data:
    d = json.load(json_data)

consumer_key=d['consumer_key']
consumer_secret=d['consumer_secret']
access_token=d['access_token']
access_token_secret=d['access_token_secret']
print(consumer_key)


