from kafka import KafkaProducer
import json

def produce_data():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    data = {'message': 'Hello Kafka'}
    producer.send('my_topic', value=data)
    producer.flush()
    print("Data sent to Kafka")
