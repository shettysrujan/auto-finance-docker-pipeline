from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    "loan_risk_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    run_spark_job = SparkSubmitOperator(
        task_id="calculate_loan_risk",
        application="/opt/airflow/spark_jobs/calculate_risk.py",
        conn_id="spark_default",
        application_args=["/opt/airflow/data/loan_applications.csv"],
        conf={
            "spark.master": "local[*]"
        }
    )
