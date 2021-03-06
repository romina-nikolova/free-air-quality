import os

# Set bit.io connection variables
os.environ['APIKEY'] = '<<apikey>>'
os.environ['CONNSTR'] = '<<connstr>>'

# Set bit.io table variables
os.environ['REPO_NAME'] = '...'
os.environ['SENSOR_TABLE_NAME'] = '...'
os.environ['SCRAPED_TABLE_NAME'] = '...'
os.environ['LOCATION_TABLE_NAME'] = '...'
os.environ['THRESHOLDS_TABLE_NAME'] = '...'

# Set additional project config variables
os.environ['SCRAPER_ONLY_FLAG'] = 'False'
os.environ['SCRAPER_URL'] = '...'
os.environ['PROCESS_SCRAPED_DATA_FLAG'] = 'True'
