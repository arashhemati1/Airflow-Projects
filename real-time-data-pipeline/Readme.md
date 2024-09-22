```perl
real-time-data-pipeline/
│
├── dags/
│   └── kafka_data_pipeline.py        # Airflow DAG definition
│
├── src/
│   ├── kafka_producer.py             # Kafka Producer script
│   ├── kafka_consumer.py             # Kafka Consumer script
│   ├── cassandra_storage.py          # Script for storing data in Cassandra
│   ├── mongodb_storage.py            # Script for storing data in MongoDB
│   ├── slack_notification.py         # Script for Slack notifications
│
├── docker-compose.yml                # Docker Compose file for services setup
│
├── requirements.txt                  # Python dependencies
│
└── README.md                         # Project description and setup instructions
