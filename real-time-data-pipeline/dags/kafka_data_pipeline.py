from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.kafka_producer import produce_data
from src.kafka_consumer import consume_data
from src.cassandra_storage import store_in_cassandra
from src.mongodb_storage import store_in_mongodb
from src.slack_notification import send_slack_alert

default_args = {
    'start_date': datetime(2024, 9, 22),
    'retries': 1,
}

def process_data():
    print("Processing data...")

dag = DAG(
    'kafka_data_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
)

produce_task = PythonOperator(
    task_id='produce_data',
    python_callable=produce_data,
    dag=dag,
)

consume_task = PythonOperator(
    task_id='consume_data',
    python_callable=consume_data,
    dag=dag,
)

process_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

cassandra_task = PythonOperator(
    task_id='store_in_cassandra',
    python_callable=store_in_cassandra,
    dag=dag,
)

mongodb_task = PythonOperator(
    task_id='store_in_mongodb',
    python_callable=store_in_mongodb,
    dag=dag,
)

slack_alert_task = PythonOperator(
    task_id='send_slack_alert',
    python_callable=send_slack_alert,
    dag=dag,
)

produce_task >> consume_task >> process_task >> [cassandra_task, mongodb_task] >> slack_alert_task
