import pandas as pd
from sqlalchemy import create_engine
import datetime


def check_last_update(connstr, scraped_table, repo):
    engine = create_engine(connstr)
    with engine.connect() as conn:
        rs = conn.execute(f"""SELECT MAX(measure_date) as last_update
                              FROM "{repo}"."{scraped_table}";""")
        return rs.fetchone()[0]


def filter_pandas_to_insert(df: pd.DataFrame, last_updated: datetime.date = datetime.date(1900, 1, 1)):
    try:
        df = df[df['measure_date'] > pd.to_datetime(last_updated)]
    except TypeError:
        return df
    return df


def load_pandas_to_bitdotio_flawed(df: pd.DataFrame, connstr: str, scraped_table: str, repo: str):
    last_updated = check_last_update(connstr, scraped_table, repo)
    df = filter_pandas_to_insert(df, last_updated)
    engine = create_engine(connstr, isolation_level="AUTOCOMMIT")
    # Append the new dataframe to the existing table
    df.to_sql(name=scraped_table,
              con=engine,
              schema=f"{repo}",
              index=False,
              if_exists='replace')


def load_pandas_to_bitdotio(df: pd.DataFrame, connstr: str, scraped_table: str, repo: str):
    last_updated = check_last_update(connstr, scraped_table, repo)
    df = filter_pandas_to_insert(df, last_updated)
    # creating column list for insertion
    cols = "`, `".join([str(i) for i in df.columns.tolist()])
    engine = create_engine(connstr, isolation_level="AUTOCOMMIT")
    # TODO: Refactor cols in sql statement
    with engine.connect() as conn:
        for i, row in df.iterrows():
            sql = f"""INSERT INTO "{repo}"."{scraped_table}"
                        (measure_date, measure_type, SO2, NO2,NO1,CO2,O3,pm10,benzene,pm2_5) 
                      VALUES('{row.measure_date}', '{row.measure_type}', {row.SO2}, {row.NO2},
                             {row.NO1},{row.CO2},{row.O3},{row.pm10},{row.benzene},{row.pm2_5})"""
            conn.execute(sql)
