# Subir o Airflow
(ok) mkdir airflow
(ok) cd airflow
(ok) curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml'
(ok) mkdir ./dags ./logs ./plugins
(ok) echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
(ok) docker-compose up airflow-init
(ok) docker-compose up
(ok) docker-compose run airflow-webserver airflow variables set 'AIRBYTE_EPIDEMIOLOGY_CONNECTION_ID' "$epidemiology_connection_id"
(ok) docker-compose run airflow-webserver airflow variables set 'AIRBYTE_ECONOMY_CONNECTION_ID' "$economy_connection_id"
(ok) docker-compose run airflow-webserver airflow variables set 'AIRBYTE_INDEX_CONNECTION_ID' "$index_connection_id"
(ok) pip install apache-airflow-providers-airbyte
(ok) docker network create data-engineering-project
(ok)(ok) docker network connect data-engineering-project airbyte-proxy
(ok)(ok) docker network connect data-engineering-project airbyte-worker  
(ok)(ok) docker network connect data-engineering-project airflow-airflow-worker-1
(ok)(ok) docker network connect data-engineering-project airflow-airflow-webserver-1)
(ok)(ok) docker network connect data-engineering-project metabase-metabase-1

