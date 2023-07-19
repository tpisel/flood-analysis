# dependencies
import pandas as pd
import requests
from urllib import parse

def get_openmeteo_data(lat: int, lon: int, start: str, end: str, api: str):
  '''
  Obtain daily data from the api for a supplied location
  `api` can be 'flood', 'weather', or 'climate change'
  '''

  if api == 'weather':
    base_url = 'https://archive-api.open-meteo.com/v1/archive?timezone=auto&'

    fields = [
      'temperature_2m_max',
      'temperature_2m_min',
      'temperature_2m_mean',
      'precipitation_sum',
      'precipitation_hours',
      'windspeed_10m_max',
      'et0_fao_evapotranspiration',
      'shortwave_radiation_sum'
      ]
    
  elif api == 'flood':
    base_url = 'https://flood-api.open-meteo.com/v1/flood?'

    fields = [
      'river_discharge'
      ]
    
  elif api == 'climate change':
    base_url = 'https://climate-api.open-meteo.com/v1/climate?models=EC_Earth3P_HR&'
    
    fields = [
        'temperature_2m_max',
        'temperature_2m_min',
        'shortwave_radiation_sum',
        'relative_humidity_2m_mean',
        'precipitation_sum',
        'et0_fao_evapotranspiration_sum'
    ]

  else:
    raise Exception("api must be: `flood` or `weather` or `climate change`")  

  request_dict = {
    'latitude': lat,
    'longitude': lon,
    'start_date': start,
    'end_date': end
  }

  query_url = (
    base_url
    + parse.urlencode(request_dict)
    + "&daily="
    + ','.join(fields)
  )
  
  try:
    response = requests.get(query_url)
  except:
    print("API call failed")

  try:
    df = pd.DataFrame(response.json()['daily'])
    dfo = df.rename(columns={'time': 'date'})
    dfo.insert(1,'latitude',lat)
    dfo.insert(2,'longitude',lon)

  except:
    print("error, check url: "+ query_url)  
  
  return dfo


def flood_and_weather_data(lat: int, lon: int, start: str, end: str):
  '''Fetch from both endpoints and combine'''

  weather_df = get_openmeteo_data(lat,lon,start,end,'weather')
  flood_df = get_openmeteo_data(lat,lon,start,end,'flood')
  joined_df = pd.merge(weather_df,flood_df,on=['date', 'latitude', 'longitude'])
  return joined_df

def agg_hourly_weather_data(lat: int, lon: int, start: str, end: str, hourly_field: str):
  '''Query a weather field not available in daily rollups and return an aggregated dataset for joining'''
  
  base_url = 'https://archive-api.open-meteo.com/v1/archive?timezone=auto&'

  request_dict = {
    'latitude': lat,
    'longitude': lon,
    'start_date': start,
    'end_date': end
  }

  query_url = (
    base_url
    + parse.urlencode(request_dict)
    + "&hourly="
    + hourly_field
  )
  
  try:
    response = requests.get(query_url)
  except:
    print("API call failed")

  try:
    df = pd.DataFrame(response.json()['hourly'])
    dfo = df.rename(columns={'time': 'date'})
    dfo.insert(1,'latitude',lat)
    dfo.insert(2,'longitude',lon)

  except:
    print("error, check url: "+ query_url)  

  # aggregate to daily
  dfo['date']=dfo.date.str[:-6]
  dfo.groupby('date').mean()

  
  return dfo

  