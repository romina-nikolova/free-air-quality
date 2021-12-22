import os
import process_scraped_data
import load_scraped_data
from time import sleep
import pandas as pd

connstr = os.getenv('CONNSTR')
scraped_table = os.getenv('SCRAPED_TABLE_NAME')
repo = os.getenv('REPO_NAME')
url = os.getenv('SCRAPER_URL')
process_flag = os.getenv('PROCESS_SCRAPED_DATA_FLAG')


if __name__ == "__main__":
    print('EXTRACT: Starting scraping...')
    os.system(
        f"scrapy runspider \
        2_scraped_air_quality/get_scraped_data.py \
        -a url={url} \
        -o file.csv \
        -t csv"
             )
    print('EXTRACT: Scraping completed.')

    sleep(4)
    if process_flag.lower() in ('true', '1', 't'):
        print('TRANSFORM: Processing scraped data...')
        df = process_scraped_data.process_scraped_data('file')
        print('TRANSFORM: Processing completed')
    else:
        df = pd.read_csv("file.csv")

    print('LOAD: Starting load to bitdotio...')
    load_scraped_data.load_pandas_to_bitdotio(df, connstr, scraped_table, repo)
    print('LOAD: Loading to bitdotio completed.')

    print('Deleting file.csv...')
    os.system("rm file.csv")
    print('Deleting file.csv completed.')
