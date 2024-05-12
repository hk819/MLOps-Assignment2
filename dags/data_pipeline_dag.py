from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.data_extraction import extract_data
from scripts.data_transformation import preprocess_text

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 12),
    'retries': 1,
}

def extract_and_transform():
    # extract data
    dawn_links, dawn_titles, dawn_descriptions = extract_data('https://www.dawn.com/')
    bbc_links, bbc_titles, bbc_descriptions = extract_data('https://www.bbc.com/')
    extracted_data = {
        'dawn': {'links': dawn_links, 'titles': dawn_titles, 'descriptions': dawn_descriptions},
        'bbc': {'links': bbc_links, 'titles': bbc_titles, 'descriptions': bbc_descriptions}
    }

    # preprocess data
    for source in extracted_data:
        for key in ['titles', 'descriptions']:
            extracted_data[source][key] = [preprocess_text(text) for text in extracted_data[source][key]]

    return extracted_data

with DAG('data_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    extract_and_transform_task = PythonOperator(
        task_id='extract_and_transform',
        python_callable=extract_and_transform
    )

extract_and_transform_task