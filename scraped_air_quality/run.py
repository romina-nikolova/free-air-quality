import os
import process_scraped_data
#import datetime
import load_scraped_data

# connstr = 'postgresql://rominanikolova1_demo_db_connection:S39t_DbapF3tAQsUqn72Lfn3SALX@db.bit.io'
# scraped_table = 'meow2'
# repo = 'rominanikolova1/ObedientSmashing'


connstr = os.environ('connstr')
scraped_table = os.environ('scraped_table')
repo = os.environ('repo')

#today = datetime.datetime.utcnow().date()
#yesterday = datetime.datetime.strftime(today - datetime.timedelta(days=1), format='%Y-%m-%d')

if __name__ == "__main__":
    print('Starting scraping...')
    os.system("scrapy runspider get_scraped_data.py -o file.csv -t csv")
    print('Scraping completed.')

    print('Processing scraped data...')
    df = process_scraped_data.process_scraped_data('file')
    print('Processing completed')

    print('Starting load to bitdotio...')
    load_scraped_data.load_pandas_to_bitdotio(df, connstr, scraped_table, repo)
    print('Loading to bitdotio completed.')

    print('Deleting file.csv...')
    os.system("rm file.csv")
    print('Deleting file.csv completed.')
