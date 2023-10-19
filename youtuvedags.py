from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import boto3
import pandas as pd
import os

# Import your YouTube ETL function
from youtubeETL import run_youtube_etl

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 10, 15),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Create the DAG
dag = DAG(
    'youtube_dag_with_s3',
    default_args=default_args,
    description='DAG to run YouTube ETL and store data in S3',
    schedule_interval=timedelta(days=1),
)

# Define the complete_youtube_etl function
def complete_youtube_etl():
    api_key = ''  # Replace with YouTube API key
    retrieved_df = run_youtube_etl(api_key)  # Pass the API key to the function

    # Define S3 bucket and file path
    s3_bucket = 'youtubeetl009'  # Replace with S3 bucket name
    s3_file_path = 'youtubevideo/DarshilP.csv'  # Replace with  desired S3 path and filename

    # Save the DataFrame to a local CSV file
    local_filename = '/tmp/local_filename.csv'
    retrieved_df.to_csv(local_filename, index=False)
    
    
  
    # Initialize the success variable
    upload_success = True

    try:
        # Upload the local CSV file to S3
      

        s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
        s3.upload_file(local_filename, s3_bucket, s3_file_path)
    except Exception as e:
        # If the upload fails, set upload_success to False and log the error
        upload_success = False
        print(f"Error uploading to S3: {str(e)}")

    if upload_success:
        print("Upload to S3 successful!")
    else:
        print("Upload to S3 failed!")

    # Clean up local files 
    os.remove(local_filename)


   

# Create a PythonOperator for running the YouTube ETL process
run_youtube_etl_task = PythonOperator(
    task_id='complete_youtube_etl',
    python_callable=complete_youtube_etl,
    dag=dag,
)

# Set the task dependency
run_youtube_etl_task


