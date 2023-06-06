#!/usr/bin/env python
# coding: utf-8
import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url

    #when the backup files are gzipped, we need correct extension for pandas to open the file

    if url.endswith('.parquet.gz'):
        file_name =  'output.parquet.gz'
    else:
        file_name = 'output.parquet'
    
    os.system(f"wget {url} -O {file_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df = pd.read_parquet(f'{file_name}', engine='pyarrow')

    print(pd.io.sql.get_schema(df,name=table_name))

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest Parquet to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)    
