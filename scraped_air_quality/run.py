import os
import process_scraped_data
from time import sleep
import datetime
import configparser
import load_scraped_data

today = datetime.datetime.utcnow().date()
yesterday = datetime.datetime.strftime(today - datetime.timedelta(days=1), format='%Y-%m-%d')


config = configparser.ConfigParser()
config.read(os.path.join(os.getenv('HOME'), 'config.ini'))

print('Starting scraping...')
#os.system("scrapy runspider get_scraped_data.py -o file.csv -t csv")
print('Scraping completed.')
print('Processing scraped data...')
df = process_scraped_data.process_scraped_data('file')
yesterday_df = df[df['measure_date'] == yesterday]
print('Processing completed')
print('Starting load to bitdotio')
load_scraped_data.load_pandas_to_bitdotio(df)
