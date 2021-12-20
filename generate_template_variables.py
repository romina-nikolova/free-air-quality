import os

# Set bit.io connection variables
os.environ['APIKEY'] = '<<apikey>>'
os.environ['CONNSTR'] = '<<connstr>>'
os.environ['HOSTNAME'] = '<<hostname>>'
os.environ['PORT'] = '<<port>>'
os.environ['DATABASE'] = '<<database>>'
os.environ['USER'] = '<<user>>'
os.environ['PASSWORD'] = '<<password>>'

# Set bit.io table variables
os.environ['REPO_NAME'] = '...'
os.environ['SENSOR_TABLE_NAME'] = '...'
os.environ['SCRAPED_TABLE_NAME'] = '...'
os.environ['LOCATION_TABLE_NAME'] = '...'
os.environ['THRESHOLDS_TABLE_NAME'] = '...'

# Set additional project config variables
os.environ['SCRAPER_ONLY_FLAG'] = 'False'
os.environ['SCRAPER_URL'] = \
    'https://www.riosv-ruse.org/danni-punktove/stantzii'
os.environ['PROCESS_SCRAPED_DATA_FLAG'] = 'True'




