from __future__ import unicode_literals
from tweepy import OAuthHandler, StreamListener, Stream
import json
import sys
import os
from kafka import KafkaClient, KafkaProducer, SimpleClient

filepath=os.path.join("creds.json")
with open(filepath,'r') as json_data:
    creds = json.load(json_data)

consumer_key=creds['consumer_key']
consumer_secret=creds['consumer_secret']
access_token=creds['access_token']
access_token_secret=creds['access_token_secret']

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

class StdOutListener(StreamListener):
    def on_data(self, raw_data):
        #producer.send("taylorsville", raw_data.encode('utf-8'))
        #print (raw_data)
        producer.send(topic="taylorsville", key=b"foo")
    def on_error(self, status_code):
        print status_code

producer = KafkaProducer(bootstrap_servers="localhost:9092")
l = StdOutListener()
stream = Stream(auth,l)
stream.filter(track="taylor", encoding='utf-8')


