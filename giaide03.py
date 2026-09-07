"""
1-A
2-A
3-A
4-A
5-A
6-A
7-A
8-A
9-A
10-A
11-A
12-A
13-A
14-A ()
15-A ()
16-A
17-A ()
18-A ()
19-A
20-A ()
21-A
22-A
23-A
24-A
25-A 
26-A
27-A()
28-A
29-A
30-A
Câu 31:
    Extract -> Validate -(nếu hợp lệ)> Transform -> Load
                        -(nếu không hợp lệ)> Alert/Fail

    retries :
    retry_delay
    dependency
    idempotency

from dattime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract_data():
    print("Extracting data...")

def validate_data():
    print("Validating data...")

def transform_data():

def load_data():
    print("Loading data...")

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
} as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    validate_task = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    extract_task >> validate_task >> transform_task >> load_task
Câu 32: 

services : 

    postgres :
        image : postgres:17
        container_name : etl_postgres

        environment :
            POSTGRES_USER : etl_user
            POSTGRES_PASSWORD : etl_password
            POSTGRES_DB : etl_db
        
        volumes :
            -postgres_data:/var/lib/postgresql/data
        
        healthcheck :
            test : ["CMD-SHELL", "pg_isready -U etl_user -d etl_db"]
            interval : 10s
            timeout : 5s
            retries : 5
        
        networks :
            - etl_network
        
    airflow :
        image : apache/airflow:2.7.1
        container_name : etl_airflow

        depends_on :
            postgres :
                condition : service_healthy

        environment :
            AIRFLOW__CORE__EXECUTOR : LocalExecutor
            AIRFLOW__CORE__SQL_ALCHEMY_CONN : postgresql+psycopg2://etl_user:etl_password@postgres:5432/etl_db
            AIRFLOW__CORE__LOAD_EXAMPLES : "False"
            AIRFLOW__API__AUTH_BACKENDS : "airflow.api.auth.backend.basic_auth"
                postgres+pycopg2://etl_user:etl_password@postgres:5432/etl_db
        
        posts :
            - 8080:8080

        volumes :
            - ./dags:/opt/airflow/dags
            - ./logs:/opt/airflow/logs
            - ./plugins:/opt/airflow/plugins

"""