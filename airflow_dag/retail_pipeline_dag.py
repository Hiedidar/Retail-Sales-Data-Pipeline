# Example Airflow DAG for the retail pipeline (requires Airflow environment)
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def task_extract(**kwargs):
    import etl.extract as ex
    ex.extract()

def task_transform(**kwargs):
    import etl.extract as ex, etl.transform as tr
    p,s,c,t = ex.extract()
    tr.transform(p,s,c,t)

def task_load(**kwargs):
    import etl.extract as ex, etl.transform as tr, etl.load as ld
    p,s,c,t = ex.extract()
    dp, ds, dc, dd, fs = tr.transform(p,s,c,t)
    ld.load(dp, ds, dc, dd, fs)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('retail_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    t1 = PythonOperator(task_id='extract', python_callable=task_extract)
    t2 = PythonOperator(task_id='transform', python_callable=task_transform)
    t3 = PythonOperator(task_id='load', python_callable=task_load)

    t1 >> t2 >> t3
