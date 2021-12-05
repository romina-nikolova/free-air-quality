import pandas as pd
import datetime
from roman import fromRoman


def convert_to_date(day: str, sep='.') -> datetime.datetime:
    """ Converts a string from format with roman month to datetime. Sample input: 21.XI.21 """
    split_date = day.split(sep)
    split_date[1] = str(fromRoman(split_date[1]))
    return datetime.datetime.strptime(sep.join(split_date), f'%d{sep}%m{sep}%y')


def process_scraped_data(filename: str):
    """ Rename columns, measure types, date format, fill NAs"""

    df = pd.read_csv(f'''{filename}.csv''')

    column_name_map = {"дата": 'measure_date',
                       "Норма/ СДК/Мах. СЧК": 'measure_type',
                       "Серен диоксид  (µg/m3)": 'SO2',
                       "Азотен диоксид (µg/m3)": 'NO2',
                       "Азотен оксид(µg/m3)": 'NO1',
                       "Въгле-роден оксид (mg/m3)": 'CO2',
                       "Озон  (µg/m3)": 'O3',
                       "Фини прахови частици под 10 микрона (µg/m3)": 'pm10',
                       "Бензен (µg/m3)": 'benzene',
                       "Фини прахови частици под 2,5 микрона(µg/m3)": 'pm2_5'}

    observation_frequency_name_map = {'СДК': 'daily_mean',
                                      'Мах.СЧК': 'hourly_max'}

    df = df.rename(columns=column_name_map)
    df['measure_type'] = df['measure_type'].replace(observation_frequency_name_map)
    df = df[df['measure_type'].isin(['daily_mean', 'hourly_max'])]
    df = df.fillna(method='ffill')
    df['measure_date'] = df['measure_date'].apply(lambda x: convert_to_date(str(x)))

    return df



