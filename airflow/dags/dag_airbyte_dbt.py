# Imports
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.models import Variable
import json

# Variaveis de ambiente
airbyte_economy_connection_id = Variable.get('AIRBYTE_ECONOMY_CONNECTION_ID')
airbyte_index_connection_id = Variable.get('AIRBYTE_INDEX_CONNECTION_ID')
airbyte_epidemiology_connection_id = Variable.get('AIRBYTE_EPIDEMIOLOGY_CONNECTION_ID')
  
# Declarando as DAG's
with DAG(  dag_id = 'trigger_airbyte_dbt_job',
           default_args = {'owner' : 'airflow'},
           schedule_interval = '@daily',
           start_date = days_ago(1)
) as dag:

    # Start economy 
    airbyte_economy_sync = AirbyteTriggerSyncOperator(
        task_id = 'airbyte_economy',
        airbyte_conn_id = 'airbyte_example',
        connection_id = airbyte_economy_connection_id,
        asynchronous = False,
        timeout = 3600,
        wait_seconds = 3
    )   

    # Start epidemiology
    airbyte_epidemiology_sync = AirbyteTriggerSyncOperator(
        task_id = 'airbyte_epidemiology',
        airbyte_conn_id = 'airbyte_example',
        connection_id = airbyte_epidemiology_connection_id,
        asynchronous = False,
        timeout = 3600,
        wait_seconds = 3
    )

    # Start index
    airbyte_index_sync = AirbyteTriggerSyncOperator(
        task_id = 'airbyte_index',
        airbyte_conn_id = 'airbyte_example',
        connection_id = airbyte_index_connection_id,
        asynchronous = False,
        timeout = 3600,
        wait_seconds = 3
    )

# Ordenação das atividade 
airbyte_index_sync >> airbyte_economy_sync >> airbyte_epidemiology_sync