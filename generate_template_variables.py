import os

# Set bit.io connection variables
os.environ['APIKEY'] = 'bladibla'
os.environ['CONNSTR'] = 'opalq'

# Set bit.io table variables
os.environ['REPO_NAME'] = 'rawr'
os.environ['SENSOR_TABLE_NAME'] = '...'
os.environ['SCRAPED_TABLE_NAME'] = 'testing_some_data'
os.environ['LOCATION_TABLE_NAME'] = '...'
os.environ['THRESHOLDS_TABLE_NAME'] = '...'

# Set additional project config variables
os.environ['SCRAPER_ONLY_FLAG'] = 'True'
os.environ['SCRAPER_URL'] = \
    'https://www.riosv-ruse.org/danni-punktove/stantzii'
os.environ['PROCESS_SCRAPED_DATA_FLAG'] = 'True'
