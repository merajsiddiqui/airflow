# from airflow import DAG
import yaml
import sys, os
from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash_operator import BashOperator
dag_yaml = os.path.dirname(os.path.dirname(__file__))+"/dags.yaml"

with open(dag_yaml, 'r') as stream:
    try:
        configuration = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)
        sys.exit(1)

default_dag_config = configuration['default']
default_dag_config['start_date']= datetime(2019, 8, 6)
dag = DAG(
    default_dag_config['id'],
    description = default_dag_config['description'],
    default_args= default_dag_config
    )

task1 = BashOperator(
    task_id = "print_date",
    bash_command='date',
    dag=dag
)