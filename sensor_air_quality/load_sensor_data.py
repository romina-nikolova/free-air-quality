import bitdotio
from datetime import datetime
import configparser
import get_sensor_data
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

now = datetime.now().replace(second=0, microsecond=0, minute=0)
today_str = now.strftime("%Y-%m-%d %H:%M:%S")

b = bitdotio.bitdotio(config['apikey'])

with b.get_connection() as conn:
    cursor = conn.cursor()

    sensor_data = get_sensor_data.get_sps30_data()
    cursor.execute(f"""INSERT INTO "{config['repo']}"."{config['sensor_data']}" (
                  date_time,
                  pm1,
                  pm2_5,
                  pm4,
                  pm10,
                  typical_size)
          VALUES ('{today_str}',
                  {sensor_data[0]},
                  {sensor_data[1]},
                  {sensor_data[2]},
                  {sensor_data[3]},
                  {sensor_data[4]}
                  )""")
    print(f"""successfully inserted sensor data for {today_str}""")