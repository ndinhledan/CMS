import requests
import json
from datetime import datetime

"""Returns the 24 hr PSI"""
def getPSI(region):

    current_datetime = str(datetime.now().isoformat(timespec='seconds'))
    url = 'https://api.data.gov.sg/v1/environment/psi?date_time=' + current_datetime

    result = requests.get(url)
    try:
        data = result.json()
        psi = data['items'][0]['readings']['psi_twenty_four_hourly'][region]

    except:
        print("Cannot fetch PSI data")

    return psi

"""Returns the weather forecast for all regions"""
def getWeather():

    current_datetime = str(datetime.now().isoformat(timespec='seconds'))
    url = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast?date_time=' + current_datetime

    result = requests.get(url)
    try:
        data = result.json()
        weather = {}
        weather['North'] = data['items'][0]['forecasts'][21]['forecast']
        weather['South'] = data['items'][0]['forecasts'][12]['forecast']
        weather['East'] = data['items'][0]['forecasts'][25]['forecast']
        weather['West'] = data['items'][0]['forecasts'][4]['forecast']
        weather['Central'] = data['items'][0]['forecasts'][8]['forecast']

    except:
        print("Cannot fetch weather data")

    return weather