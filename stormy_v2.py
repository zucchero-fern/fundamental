# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 08:23:57 2022

@author: lucas.silva
"""
import pandas as pd
import urllib.request, time, datetime
from io import StringIO
import matplotlib.pyplot as plt

## Settings
#apikey = '186293f381b0e52ee1f17b3114df9eb' # Ken's
apikey = '1ecaf626dc01a657371e618257ab7e0e' # TJ's

baseURL = 'https://api.stormvistawxmodels.com/v1/model-data/'

## Function to download/wait until file exists
def downloadFile(url):
  downloaded = False
  while not downloaded:
    try:
      resp = urllib.request.urlopen(url)
    except:
      print('File not found...waiting for {url}'.format(url=url))
      time.sleep(300)
    else:
      print('Downloaded {url}'.format(url=url))
      downloaded = True
  return resp.read()



def load_stations():
    africa_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-africa.csv')
    aus_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-australia.csv')
    #na_stations = pd.read_csv('C:\Users\lucas.silva\lucas_grains\weather\station-list-northamerica.csv')
    soam_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-southamerica.csv')
    eu_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-europe.csv')
    asia_station = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-asia.csv')
