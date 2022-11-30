# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:35:34 2022

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


africa_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-africa.csv')
aus_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-australia.csv')
#na_stations = pd.read_csv('C:\Users\lucas.silva\lucas_grains\weather\station-list-northamerica.csv')
soam_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-southamerica.csv')
eu_stations = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-europe.csv')
asia_station = pd.read_csv('\\Users\lucas.silva\lucas_grains\weather\station-list-asia.csv')

#IA= north_america_station[north_america_station.State == ' IA']
#IL= north_america_station[north_america_station.State == ' IL']
#IN= north_america_station[north_america_station.State == ' IN']
#KS= north_america_station[north_america_station.State == ' KS']
#MI= north_america_station[north_america_station.State == ' MI']
#MN= north_america_station[north_america_station.State == ' MN']
#MO= north_america_station[north_america_station.State == ' MO']
#ND= north_america_station[north_america_station.State == ' ND']
#NE= north_america_station[north_america_station.State == ' NE']
#OH= north_america_station[north_america_station.State == ' OH']
#SD= north_america_station[north_america_station.State == ' SD']
#WI= north_america_station[north_america_station.State == ' WI']





#Sao_Paolo = pd.DataFrame(SP)
#SP_Count = Sao_Paolo.reset_index().station.nunique()
#SP_Precip = (Sao_Paolo.precip.sum()/(SP_Count*precip_adjustment)).round()





################################################################# CURRENT MODEL
'''Date of model run'''
Y = 2022
m= 4
d= 13
h= 12

fileDate = datetime.datetime(Y,m,d,h) # Y,m,d,h

## City Extraction North America Daily Max/Min for ECMWF-EPS
#fileName = '{model}/{date}/{cycle}z/city-extraction/max-min_{region}.csv?apikey={apikey}' \
#            .format(model="gfs", \
#                    date=fileDate.strftime("%Y%m%d"), \
#                    cycle=fileDate.strftime("%H"), \
#                    region="southamerica", \
#                    apikey=apikey)
#modelData = downloadFile('{baseURL}{fileName}' \
#                          .format(baseURL=baseURL,fileName=fileName))
#

'''Model Selection'''

weather_model = "gfs"
# (gfs, gfs-ens, ecmwf, ecmwf-eps), (cmc, cmc-ens) cmc only works for analogs
# ecmwf at 0/18 z is only 90 hours and ecmwf-eps is 144 hours

fileName1 = '{model}/{date}/{cycle}z/city-extraction/realtime-all-stations-hourly_{region}.csv?apikey={apikey}' \
            .format(model=weather_model, \
                    date=fileDate.strftime("%Y%m%d"), \
                    cycle=fileDate.strftime("%H"), \
                    region="southamerica", \
                    apikey=apikey)
modelData = downloadFile('{baseURL}{fileName1}' \
                          .format(baseURL=baseURL,fileName1=fileName1))

#fileName1 = '{model}/{date}/{cycle}z/city-extraction/all-stations-hourly-postproc_{region}.csv?apikey={apikey}' \
#            .format(model=weather_model, \
#                    date=fileDate.strftime("%Y%m%d"), \
#                    cycle=fileDate.strftime("%H"), \
#                    region="southamerica", \
#                    apikey=apikey)
#modelData = downloadFile('{baseURL}{fileName1}' \
#                          .format(baseURL=baseURL,fileName1=fileName1))



type(modelData)




s=str(modelData,'utf-8')
data = StringIO(s)
df=pd.read_csv(data)
weather_df = df.set_index('station')

###### Current Model's Precip
precip_adjustment = 1
mato_grosso_stations = list(soam_stations[soam_stations.State == 'Mato Grosso']['Station'])
mato_grosso_data = weather_df.loc[mato_grosso_stations]
mato_grosso_count = mato_grosso_data.reset_index().station.nunique()
mato_grosso_precip = (mato_grosso_data.precip.sum()/(mato_grosso_count*precip_adjustment)).round()

sao_paulo_stations = list(soam_stations[soam_stations.State == 'Sao Paulo']['Station'])
sao_paulo_data = weather_df.loc[sao_paulo_stations]
sao_paulo_count = sao_paulo_data.reset_index().station.nunique()
sao_paulo_precip = (sao_paulo_data.precip.sum()/(sao_paulo_count*precip_adjustment)).round()

################################################################ PREVIOUS MODEL
'''Date of model run'''
Y = 2022
m = 4
d = 12
h_ = 0

fileDate_ = datetime.datetime(Y, m, d, h_) # Y,m,d,h

## City Extraction North America Daily Max/Min for ECMWF-EPS
#fileName = '{model}/{date}/{cycle}z/city-extraction/max-min_{region}.csv?apikey={apikey}' \
#            .format(model="gfs", \
#                    date=fileDate.strftime("%Y%m%d"), \
#                    cycle=fileDate.strftime("%H"), \
#                    region="southamerica", \
#                    apikey=apikey)
#modelData = downloadFile('{baseURL}{fileName}' \
#                          .format(baseURL=baseURL,fileName=fileName))
#

'''Model Selection'''

weather_model = "gfs"
# (gfs, gfs-ens, ecmwf, ecmwf-eps), (cmc, cmc-ens) cmc only works for analogs
# ecmwf at 0/18 z is only 90 hours and ecmwf-eps is 144 hours

fileName1_ = '{model}/{date}/{cycle}z/city-extraction/realtime-all-stations-hourly_{region}.csv?apikey={apikey}' \
            .format(model=weather_model, \
                    date=fileDate_.strftime("%Y%m%d"), \
                    cycle=fileDate_.strftime("%H"), \
                    region="southamerica", \
                    apikey=apikey)
modelData_ = downloadFile('{baseURL}{fileName1}' \
                          .format(baseURL=baseURL,fileName1=fileName1_))

#fileName1 = '{model}/{date}/{cycle}z/city-extraction/all-stations-hourly-postproc_{region}.csv?apikey={apikey}' \
#            .format(model=weather_model, \
#                    date=fileDate.strftime("%Y%m%d"), \
#                    cycle=fileDate.strftime("%H"), \
#                    region="southamerica", \
#                    apikey=apikey)
#modelData = downloadFile('{baseURL}{fileName1}' \
#                          .format(baseURL=baseURL,fileName1=fileName1))



type(modelData_)




s_=str(modelData_,'utf-8')
data_ = StringIO(s_)
df_ =pd.read_csv(data_)
weather_df_ = df_.set_index('station')


precip_adjustment = 1


### Previous
# mato_grosso_stations = list(soam_stations[soam_stations.State == 'Mato Grosso']['Station'])
mato_grosso_data_ = weather_df_.loc[mato_grosso_stations]
mato_grosso_count_ = mato_grosso_data_.reset_index().station.nunique()
mato_grosso_precip_ = (mato_grosso_data_.precip.sum()/(mato_grosso_count_*precip_adjustment)).round()

sao_paulo_stations = list(soam_stations[soam_stations.State == 'Sao Paulo']['Station'])
sao_paulo_data = weather_df.loc[sao_paulo_stations]
sao_paulo_count = sao_paulo_data.reset_index().station.nunique()
sao_paulo_precip = (sao_paulo_data.precip.sum()/(sao_paulo_count*precip_adjustment)).round()

plt.figure(figsize=(12, 8))
plt.plot(mato_grosso_precip)
plt.plot(sao_paulo_precip)
plt.show()

######

'''State Weather Station Weights'''

sp_1 = weather_df.loc[['SBKP', 'SBFC', 'SBRP', 'SBFT', 'SBSR', 'SBUP', 'SBDN', 'SBAS', 'SBBU']]
Sao_Paolo = pd.DataFrame(SP)
SP_Count = Sao_Paolo.reset_index().station.nunique()
SP_Precip = (Sao_Paolo.precip.sum()/(SP_Count*precip_adjustment)).round()

MG= weather_df.loc[['SBIT', 'SBUL', 'SBUR', 'SBFU', 'SBVG', 'SBIP']]
Minas_Gerias = pd.DataFrame(MG)
MG_Count = Minas_Gerias.reset_index().station.nunique()
MG_Precip = (Minas_Gerias.precip.sum()/(MG_Count*precip_adjustment)).round()


RS= weather_df.loc[['SBNM', 'SBPF', 'SBSM', 'SBCX', 'SBUG', 'SBBG', 'SBRV', 'SBCH']]
RGDS = pd.DataFrame(RS)
RS_Count = RGDS.reset_index().station.nunique()
RS_Precip = (RGDS.precip.sum()/(RS_Count*precip_adjustment)).round()


PR= weather_df.loc[['SBCA', 'SBMG', 'SBLO', 'SBTL', 'SBGS']]
Parana = pd.DataFrame(PR)
PR_Count = Parana.reset_index().station.nunique()
PR_Precip = (Parana.precip.sum()/(PR_Count*precip_adjustment)).round()


Cordoba= weather_df.loc[['SACO', 'SAOC', 'SAOL', 'SAOR', 'SAOM']]
Cordoba_Argentina = pd.DataFrame(Cordoba)
Cordoba_Count = Cordoba_Argentina.reset_index().station.nunique()
Cordoba_Arg_Precip = (Cordoba_Argentina.precip.sum()/(Cordoba_Count*precip_adjustment)).round()


Santa_Fe= weather_df.loc[['SAAR', 'SAAV', 'SAAP', 'SANW', 'SATR']]
Santa_Fe_Argentina = pd.DataFrame(Santa_Fe)
Santa_Fe_Count = Santa_Fe_Argentina.reset_index().station.nunique()
SF_Arg_Precip = (Santa_Fe_Argentina.precip.sum()/(Santa_Fe_Count*precip_adjustment)).round()

BA= weather_df.loc[['SAAJ', 'SAEZ', 'SAZ1', 'SAZT', 'SAZB', 'SAZR']]
BA_Argentina = pd.DataFrame(BA)
BA_Count = BA_Argentina.reset_index().station.nunique()
BA_Arg_Precip = (BA_Argentina.precip.sum()/(BA_Count*precip_adjustment)).round()

print('{} is {} mm basis the {} model {}z run'.format("SP", SP_Precip, weather_model,h))
print('{} is {} mm basis the {} model {}z run'.format("MG", MG_Precip, weather_model,h))
print('{} is {} mm basis the {} model {}z run'.format("RS", RS_Precip, weather_model,h))
print('{} is {} mm basis the {} model {}z run'.format("PR", PR_Precip, weather_model,h))
print('{} is {} mm basis the {} model {}z run'.format("Cordoba_Arg", Cordoba_Arg_Precip, weather_model,h))
print('{} is {} mm basis the {} model {}z run'.format("Santa_Fe_Arg", SF_Arg_Precip, weather_model,h))
print('{} is {} mm basis the {} model {}z run'.format("BA_Arg", BA_Arg_Precip, weather_model,h))
