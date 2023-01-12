from dotenv import load_dotenv
load_dotenv()
from sparkbike.download_utils import zip_write, sqlconnector
import os
import pandas as pd
try:
    sqlconnector("SELECT 1 FROM stations;")
except:
    zip_write()
    pd.read_csv(os.getenv('station_path'), header=1).to_csv(os.getenv('station_path_local'))
    os.system("curl -o {} {}".format(os.getenv('station_path'),os.getenv('journey_path_local')))
    os.system("csvsql --db {} --tables stations --insert {}".format(os.getenv('postgresql_db'),os.getenv('station_path_local')))
    os.system("csvsql --db {} --tables journeys --insert {}".format(os.getenv('postgresql_db'),os.getenv('journey_path_local')))

