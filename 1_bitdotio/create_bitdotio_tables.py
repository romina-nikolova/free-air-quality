from sqlalchemy import create_engine
import os

connstr = os.environ['CONNSTR']
repo = os.environ['REPO_NAME']
scraper_only_flag = os.environ['SCRAPER_ONLY_FLAG']

engine = create_engine(connstr, isolation_level="AUTOCOMMIT")


def execute_bitdotio_sql(create_sql_file_name,
                         engine,
                         repo,
                         table):
    with engine.connect() as conn:
        sql_statement = open(create_sql_file_name)\
            .read()\
            .replace('repo', repo)\
            .replace('table', table)
        conn.execute(sql_statement)


if __name__ == "__main__":
    engine = create_engine(connstr, isolation_level="AUTOCOMMIT")
    print('Creating tables')
    execute_bitdotio_sql('create_table_scraped_data.sql',
                         engine, repo, 'scraped_data')

    if scraper_only_flag.lower() in ('true', '1', 't'):
        execute_bitdotio_sql('create_table_location.sql',
                             engine, repo, 'location')
        execute_bitdotio_sql('create_table_sensor_data.sql',
                             engine, repo, 'sps30')
        execute_bitdotio_sql('create_table_thresholds.sql',
                             engine, repo, 'thresholds')

        print('Inserting data into location')
        execute_bitdotio_sql('insert_table_location.sql',
                             engine, repo, 'location')

        print('Inserting data into thresholds')
        execute_bitdotio_sql('insert_table_thresholds.sql',
                             engine, repo, 'thresholds')
