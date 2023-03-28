# Import
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils import timezone
import logging

# Define DAG
dag = DAG(
    'helloX',
    default_args={'owner': 'Ton'},
    schedule_interval='*/30 * * * *',
    start_date=timezone.datetime(2020, 12, 12),
    catchup=False
)

def hello():
    return 'Hello, Python'

def print_log_messages():
    logging.debug('This is a debug message')
    return 'Wharwver ..'


# Define operators and tasks
start = DummyOperator(
    task_id='start',
    dag=dag,
)
echo_hello = BashOperator(
    task_id='echo_hello',
    bash_command = 'echo hello',
    dag=dag,
)
say_hello = PythonOperator(
    task_id='say_hello',
    python_callable=hello,
    dag=dag,
)
print_log_messages = PythonOperator(
    task_id='print_log_messages',
    python_callable=print_log_messages,
    dag=dag,
)
end = DummyOperator(
    task_id='end',
    dag=dag,
)

# Define dependencies
start >> echo_hello >> say_hello >> print_log_messages >> end