docker pull puckel/docker-airflow;
docker run -d -p 8080:8080 -e LOAD_EX=y puckel/docker-airflow webserver;

# In your browser open localhost:8080
