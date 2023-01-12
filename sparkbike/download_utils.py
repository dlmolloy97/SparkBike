import pandas as pd
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
import os
import zipfile

def zip_write():
    os.system("wget {} -P data/".format(os.getenv("zip_path")))
    with zipfile.ZipFile("data/202211-bluebikes-tripdata.zip", 'r') as zip_ref:
        zip_ref.extractall("data/")

def journey_get():
    pd.read_csv(os.getenv('station_path'), header=True)



def sqlconnector(query):
    alchemyEngine = create_engine(os.getenv('postgresql_path'), pool_recycle=3600)
    dbConnection = alchemyEngine.connect()
    return pd.read_sql(query, dbConnection)
