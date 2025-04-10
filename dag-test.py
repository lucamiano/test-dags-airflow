from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging

def stampa_log():
    logging.info("This is a message from Airflow.")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 10),
    'retries': 1,
}

with DAG(
    dag_id='test-dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    task_stampa_log = PythonOperator(
        task_id='stampa_log',
        python_callable=stampa_log,
    )
