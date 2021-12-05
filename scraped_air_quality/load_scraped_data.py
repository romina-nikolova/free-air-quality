import pandas as pd
import datetime
from sqlalchemy import create_engine
import configparser
from process_scraped_data import process_scraped_data
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
print(config)
today = datetime.datetime.utcnow().date()
yesterday = datetime.datetime.strftime(today - datetime.timedelta(days=1), format='%Y-%m-%d')


def load_pandas_to_bitdotio(df: pd.DataFrame):
    engine = create_engine(config['bitdotio']['connstr'])
    # Append the new dataframe to the existing table
    with engine.connect() as conn:
        df.to_sql(
            config['bitdotio']['scraped_table'],
            conn,
            schema=f"{config['bitdotio']['repo']}",
            index=False,
            if_exists='append')
        print(f'successfully inserted sensor data for {yesterday}')
