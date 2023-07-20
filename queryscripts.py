# dependencies
import pandas as pd
import requests
from urllib import parse

def get_openmeteo_data(lat: int, lon: int, start: str, end: str, api: str):
  '''
  Obtain daily data from the api for a supplied location
  `api` can be 'flood', 'weather'
  '''

  if api == 'weather':
    base_url = 'https://archive-api.open-meteo.com/v1/archive?timezone=auto&'

    fields = [
      'temperature_2m_max',
      'temperature_2m_min',
      'temperature_2m_mean',
      'precipitation_sum',
      'precipitation_hours',
      'windspeed_10m_max'
      ]
    
  elif api == 'flood':
    base_url = 'https://flood-api.open-meteo.com/v1/flood?'

    fields = [
      'river_discharge'
      ]
    
  else:
    raise Exception("api must be: `flood` or `weather`")  

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
  except:
    print("error, check url: "+ query_url)
  
  dfo = df.rename(columns={'time': 'date'})
  dfo.insert(1,'latitude',lat)
  dfo.insert(2,'longitude',lon)

  return dfo


def flood_and_weather_data(lat: int, lon: int, start: str, end: str):
  '''Fetch from both endpoints and combine'''

  weather_df = get_openmeteo_data(lat,lon,start,end,'weather')
  flood_df = get_openmeteo_data(lat,lon,start,end,'flood')
  joined_df = pd.merge(weather_df,flood_df,on=['date', 'latitude', 'longitude'])
  return joined_df