from kafka import KafkaConsumer
import json
import os
from kafka import TopicPartition

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=1000
                         )
consumer.subscribe(['taylorsville'])
for message in consumer:
    print(message)

consumer.close()