from kafka import KafkaConsumer
import json

def consume_data():
    consumer = KafkaConsumer(
        'my_topic',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        print(f"Received: {message.value}")
