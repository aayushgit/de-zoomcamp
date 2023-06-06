# base Docker image that we will build on
FROM python:3.9.1

# set up our image by installing prerequisites;
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2-binary pyarrow

# set up the working directory inside the container
WORKDIR /app
# copy the script to the container. 1st name is source file, 2nd is destination
COPY ingest_data.py ingest_data.py

# define what to do first when the container runs
# in this example, we will just run the script
ENTRYPOINT ["python", "ingest_data.py"]