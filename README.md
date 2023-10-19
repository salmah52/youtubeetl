# Youtubeetl
# YouTube Data ETL with Airflow

## Project Overview

The **YouTube Data ETL with Airflow** project is an end-to-end data pipeline designed to automate the extraction, transformation, and loading of data from YouTube channels. It integrates with the YouTube Data API, extracts data, processes it, and allows you to choose a destination for storage, which can include Amazon S3, Google Cloud Storage, or other storage solutions.

## Architecture

<img width="646" alt="image" src="https://github.com/salmah52/youtubeetl/assets/44398948/8cdd48b9-b9d7-47fd-a6fb-bc6ddb814fbc">


## Project Components

This project is comprised of several key components, with each playing a crucial role in ensuring the data from YouTube channels is efficiently processed and organized. The main components include:

- **Data Extraction:** Leveraging the YouTube Data API, I fetch data from specific YouTube channels. For my project, I've been using the "DarshilParmar" channel. It's important to note that during the development process, I faced challenges related to the API's query timeout and rate limiting, resulting in intermittent failures and time-outs.

- **Data Transformation:** The extracted data is transformed into a structured format suitable for analysis. 

- **Data Loading:** Once the data is prepared, you can choose the destination for storage. In my project, I have configured data to be stored in an Amazon S3 bucket. However, you have the flexibility to choose other cloud storage solutions like Google Cloud Storage.

- **Airflow Integration:** This project is integrated with Apache Airflow, allowing for scheduled or trigger-based ETL jobs. This integration has been instrumental in automating and orchestrating the entire pipeline. In the process, I have encountered and resolved issues such as configuring Airflow DAGs and tasks for reliable execution.

- **Error Handling:** Robust error handling mechanisms are in place to ensure the pipeline gracefully handles exceptions and provides clear notifications of any issues. I have improved error handling and provided detailed logging to facilitate troubleshooting when errors occur.

## Project Goals

The primary goals of this project include:

- Automating the collection of data from YouTube channels. My project's channel of choice has been "DarshilParmar".

- Ensuring the collected data is clean, structured, and ready for analysis. I have implemented data cleaning and structuring functions.

- Allowing flexibility in choosing the destination for storing the data. My project's setup stores data in an Amazon S3 bucket, and it's adaptable to other cloud storage solutions.

- Implementing an efficient and reliable ETL process that can be scheduled and monitored. I have incorporated scheduling using Apache Airflow.

- Providing a framework for expanding the ETL process and customizing it as per specific requirements. 



