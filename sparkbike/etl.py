from dotenv import load_dotenv
import os
import zipfile
import pandas as pd
from geopandas import GeoDataFrame, read_file
import geopandas

class ExtractTransformLoad:
    def __init__(self):
        pass

    def zip(self):
        load_dotenv()
        with zipfile.ZipFile(os.getenv("zip_path"), 'r') as zip_ref:
            zip_ref.extractall("data/")

    def geojoin(self):
        polydf = read_file('data/Boston_Neighborhoods.geojson')

        stations = pd.read_csv(os.getenv("station_path"), header=1)


        pointdf = GeoDataFrame(
            stations, geometry=geopandas.points_from_xy(stations.Longitude, stations.Latitude))

        pointdf.set_crs(epsg='4326', inplace=True)
        assert polydf.crs == pointdf.crs
        joined_df = pointdf.sjoin(polydf, how="left")
        matched_pairs = joined_df[joined_df['District']=='Boston'][['Name_left', 'Name_right']].drop_duplicates()
        matched_pairs.columns = ['Station', 'Neighbourhood']
        matched_pairs.to_csv('data/neighbourhood_stations.csv')

