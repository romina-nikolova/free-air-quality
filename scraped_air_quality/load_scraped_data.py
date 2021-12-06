import pandas as pd
from sqlalchemy import create_engine


def load_pandas_to_bitdotio(df: pd.DataFrame, connstr: str, scraped_table: str, repo: str):
    engine = create_engine(connstr)
    # Append the new dataframe to the existing table
    with engine.connect() as conn:
        df.to_sql(
            scraped_table,
            conn,
            schema=f"{repo}",
            index=False,
            if_exists='append')
