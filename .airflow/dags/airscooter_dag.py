
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2017, 8, 22),
    'schedule_interval': '@once',
}

dag = DAG('airscooter_dag', default_args=default_args, schedule_interval=timedelta(1))
    

depositor = BashOperator(bash_command="python /home/alex/Desktop/airscooter-quickstart-example/depositor.py", task_id="depositor", dag=dag)

transform = BashOperator(bash_command="python /home/alex/Desktop/airscooter-quickstart-example/transform.py", task_id="transform", dag=dag)
transform.set_upstream(depositor)
