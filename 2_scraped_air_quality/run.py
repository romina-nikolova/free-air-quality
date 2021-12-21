import os
import process_scraped_data
import load_scraped_data
from time import sleep

connstr = os.getenv('CONNSTR')
scraped_table = os.getenv('SCRAPED_TABLE_NAME')
repo = os.getenv('REPO_NAME')
url = os.getenv('SCRAPER_URL')


if __name__ == "__main__":
    print('Starting scraping...')
    os.system(
        f"scrapy runspider \
        2_scraped_air_quality/get_scraped_data.py \
        -a url={url} \
        -o file.csv \
        -t csv"
             )
    print('Scraping completed.')

    sleep(4)

    print('Processing scraped data...')
    df = process_scraped_data.process_scraped_data('file')
    print('Processing completed')

    print('Starting load to bitdotio...')
    load_scraped_data.load_pandas_to_bitdotio(df, connstr, scraped_table, repo)
    print('Loading to bitdotio completed.')

    print('Deleting file.csv...')
    os.system("rm file.csv")
    print('Deleting file.csv completed.')
