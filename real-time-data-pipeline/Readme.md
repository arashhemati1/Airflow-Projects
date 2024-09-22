# Real-Time Data Pipeline

This project implements a real-time data processing pipeline using Apache Kafka, Apache Airflow, Python, and NoSQL databases like Cassandra and MongoDB. It is designed to be flexible, scalable, and suitable for various applications, from e-commerce to IoT.

## Features

- **Real-time Data Ingestion** with Kafka
- **Workflow Orchestration** using Airflow
- **Data Storage** in Cassandra and MongoDB
- **Slack Notifications** for monitoring
- **Docker** for easy deployment

## Setup Instructions

1. Clone the repository:
   ```bash
      git clone https://github.com/yourusername/real-time-data-pipeline.git
      cd real-time-data-pipeline

## Install Python dependencies:
      ```bash
           pip install -r requirements.txt

## Start the services using Docker Compose
      ```bash
           docker-compose up


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
