# Import
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils import timezone

# Define DAG
dag = DAG(
    'my_first_dag',
    default_args={'owner': 'Ton'},
    schedule_interval='* * * * *',
    start_date=timezone.datetime(2020, 12, 12)
)


# Define operators and tasks
t1 = DummyOperator(
    task_id='t1',
    dag=dag,
)
t2 = DummyOperator(
    task_id='t2',
    dag=dag,
)


# Define dependencies
t1 >> t2