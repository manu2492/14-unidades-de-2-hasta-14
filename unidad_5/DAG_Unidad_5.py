# import the libraries
import logging as log
import os
from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import pandas as pd

# dir
DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/dags')


# create logger
logger = log.getLogger("airflow.task")


# defining DAG arguments

default_args = {
    'retries': 5,
    'retry_delay': timedelta(seconds=5),
}


# Tasks
def read_top10():

    # Read CSV from web
    #url = F"{DIR}/medals.csv"
    url = "http://winterolympicsmedals.com/medals.csv"
    try:
        logger.info("reading")
        df = pd.read_csv(url)

        # Get top 10 countries with most medals
        logger.info("procesing")
        top_countries = df.NOC.value_counts().sort_values(ascending=False).head(10)

        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()

        # Save data frame in Excel format - Completar tu propia ubicación para guardar el archivo de salida
        logger.info("sabing")

        to_countries_df.to_excel(f'{DIR}/top10_medals_by_country.xlsx')

        logger.info("Success")
    except Exception:
        logger.error("Fail")


def process():
    pass


def process2():
    pass


# task pipeline

with DAG(
    'DAG_tema_5',
    default_args=default_args,
    description='el dag de manu',
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2022, 10, 10)
) as dag:
    query = PythonOperator(task_id='query',
                           python_callable=read_top10) 
    pandas_process = PythonOperator(task_id='pandas_process',
                                    python_callable=process)
    load = PythonOperator(task_id='load',
                          python_callable=process2)

    query >> pandas_process >> load





   
