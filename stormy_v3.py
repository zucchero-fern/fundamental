# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:54:00 2022

@author: lucas.silva
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:13:31 2022

@author: townsend.lansburg
"""



import pandas as pd
import urllib.request, time, datetime
from io import StringIO 
from datetime import date

## Settings

apikey = '1ecaf626dc01a657371e618257ab7e0e'
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
 

north_america_station = pd.read_csv('C://Users//Lucas.Silva//lucas_grains//weather//stations_stormvista//station-list-northamerica.csv')
south_america_station = pd.read_csv('C://Users//Lucas.Silva//lucas_grains//weather//stations_stormvista//station-list-southamerica.csv')
europe_station = pd.read_csv('C://Users//Lucas.Silva//lucas_grains//weather//stations_stormvista//station-list-europe.csv')
asia_station = pd.read_csv('C://Users//Lucas.Silva//lucas_grains//weather//stations_stormvista//station-list-asia.csv')


'''South America Stations'''

Paraguay_Stations = south_america_station[south_america_station.State == ' Paraguay']
Uruguay_Stations = south_america_station[south_america_station.State == ' Uruguay']

'''Argentina'''
BA_Arg_Stations = south_america_station[south_america_station.State == 'Buenos_Aires']
Cordoba_Arg_Stations = south_america_station[south_america_station.State == 'Cordoba']
Santa_Fe_Arg_Stations = south_america_station[south_america_station.State == 'Santa_Fe']
Entre_Rios_Arg_Stations = south_america_station[south_america_station.State == 'Entre_Rios']
La_Pampa_Arg_Stations = south_america_station[south_america_station.State == 'La_Pampa']
Salta_Arg_Stations = south_america_station[south_america_station.State == 'Salta']
San_Luis_Arg_Stations = south_america_station[south_america_station.State == 'San_Luis']

'''Brazil'''
RS_Stations = south_america_station[south_america_station.State == 'RS']
PR_Stations = south_america_station[south_america_station.State == 'PR']
SP_Stations = south_america_station[south_america_station.State == 'SP']
MG_Stations = south_america_station[south_america_station.State == 'MG']
MT_Stations = south_america_station[south_america_station.State == 'MT']
GO_Stations = south_america_station[south_america_station.State == 'GO']
MS_Stations = south_america_station[south_america_station.State == 'MS']

## Common settings
'''Date of model run'''

today = date.today()

Y = today.year
m= today.month
d= today.day
h=  12

#Y = 2022
#m= 1
#d= 27
#h= 0


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
df['stations'] = df.station.copy()
weather_df = df.set_index('station')
weather_df['DATETIME'] = fileDate + pd.to_timedelta(weather_df['fhr'], unit = 'h')
weather_df['Date'] = weather_df['DATETIME'].dt.strftime("%m/%d/%Y")

'''State Weather Station Weights'''

precip_adjustment = 1



''' South America Code'''

Paraguay= weather_df.loc[Paraguay_Stations.Station]
Paraguay_Weather = pd.DataFrame(Paraguay)
Paraguay_Weather['precip_mm'] = Paraguay_Weather.precip * 1
Paraguay_Count = Paraguay_Weather.reset_index().station.nunique()
Paraguay_Precip = (Paraguay_Weather.precip.sum()/(Paraguay_Count*precip_adjustment)).round(1)
Paraguay_1_5_Day = ((Paraguay_Weather[(Paraguay_Weather.fhr<=120)].precip.sum())/((Paraguay_Count*precip_adjustment))).round(1)
Paraguay_6_10_Day = ((Paraguay_Weather[(Paraguay_Weather.fhr>120)&(Paraguay_Weather.fhr<=240)].precip.sum())/((Paraguay_Count*precip_adjustment))).round(1)
Paraguay_11_15_Day = ((Paraguay_Weather[(Paraguay_Weather.fhr>240)].precip.sum())/((Paraguay_Count*precip_adjustment))).round(1)
Paraguay_Weather_precip_Forecast = Paraguay_Weather.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Paraguay_Weather_Forecast = Paraguay_Weather_precip_Forecast.groupby(['Date']).mean()
Paraguay_Weather_Forecast_Mean = Paraguay_Weather.groupby(['Date', 'stations']).tmp2m.mean()
Paraguay_Weather_Forecast_Mean_Temp = Paraguay_Weather_Forecast_Mean.groupby(['Date']).mean()
Paraguay_Weather_Forecast_Max = Paraguay_Weather.groupby(['Date','stations']).tmp2m.max()
Paraguay_Weather_Forecast_Max_Temp =Paraguay_Weather_Forecast_Max.groupby(['Date']).mean()
Paraguay_Weather_Forecast_Min = Paraguay_Weather.groupby(['Date','stations']).tmp2m.min()
Paraguay_Weather_Forecast_Min_Temp = Paraguay_Weather_Forecast_Min.groupby(['Date']).mean()

Uruguay= weather_df.loc[Uruguay_Stations.Station]
Uruguay_Weather = pd.DataFrame(Uruguay)
Uruguay_Weather['precip_mm'] = Uruguay_Weather.precip * 1
Uruguay_Count = Uruguay_Weather.reset_index().station.nunique()
Uruguay_Precip = (Uruguay_Weather.precip.sum()/(Uruguay_Count*precip_adjustment)).round(1)
Uruguay_1_5_Day = ((Uruguay_Weather[(Uruguay_Weather.fhr<=120)].precip.sum())/((Uruguay_Count*precip_adjustment))).round(1)
Uruguay_6_10_Day = ((Uruguay_Weather[(Uruguay_Weather.fhr>120)&(Uruguay_Weather.fhr<=240)].precip.sum())/((Uruguay_Count*precip_adjustment))).round(1)
Uruguay_11_15_Day = ((Uruguay_Weather[(Uruguay_Weather.fhr>240)].precip.sum())/((Uruguay_Count*precip_adjustment))).round(1)
Uruguay_Weather_precip_Forecast = Uruguay_Weather.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Uruguay_Weather_Forecast = Uruguay_Weather_precip_Forecast.groupby(['Date']).mean()
Uruguay_Weather_Forecast_Mean = Uruguay_Weather.groupby(['Date', 'stations']).tmp2m.mean()
Uruguay_Weather_Forecast_Mean_Temp = Uruguay_Weather_Forecast_Mean.groupby(['Date']).mean()
Uruguay_Weather_Forecast_Max = Uruguay_Weather.groupby(['Date','stations']).tmp2m.max()
Uruguay_Weather_Forecast_Max_Temp =Uruguay_Weather_Forecast_Max.groupby(['Date']).mean()
Uruguay_Weather_Forecast_Min = Uruguay_Weather.groupby(['Date','stations']).tmp2m.min()
Uruguay_Weather_Forecast_Min_Temp = Uruguay_Weather_Forecast_Min.groupby(['Date']).mean()


SP= weather_df.loc[SP_Stations.Station]
Sao_Paolo = pd.DataFrame(SP)
Sao_Paolo['precip_mm'] = Sao_Paolo.precip * 1
SP_Count = Sao_Paolo.reset_index().station.nunique()
SP_Precip = (Sao_Paolo.precip.sum()/(SP_Count*precip_adjustment)).round(1)
SP_1_5_Day = ((Sao_Paolo[(Sao_Paolo.fhr<=120)].precip.sum())/((SP_Count*precip_adjustment))).round(1)
SP_6_10_Day = ((Sao_Paolo[(Sao_Paolo.fhr>120)&(Sao_Paolo.fhr<=240)].precip.sum())/((SP_Count*precip_adjustment))).round(1)
SP_11_15_Day = ((Sao_Paolo[(Sao_Paolo.fhr>240)].precip.sum())/((SP_Count*precip_adjustment))).round(1)
Sao_Paolo_precip_Forecast = Sao_Paolo.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Sao_Paolo_Forecast = Sao_Paolo_precip_Forecast.groupby(['Date']).mean()
Sao_Paolo_Forecast_Mean = Sao_Paolo.groupby(['Date', 'stations']).tmp2m.mean()
Sao_Paolo_Forecast_Mean_Temp = Sao_Paolo_Forecast_Mean.groupby(['Date']).mean()
Sao_Paolo_Forecast_Max = Sao_Paolo.groupby(['Date','stations']).tmp2m.max()
Sao_Paolo_Forecast_Max_Temp =Sao_Paolo_Forecast_Max.groupby(['Date']).mean()
Sao_Paolo_Forecast_Min = Sao_Paolo.groupby(['Date','stations']).tmp2m.min()
Sao_Paolo_Forecast_Min_Temp = Sao_Paolo_Forecast_Min.groupby(['Date']).mean() 


MG= weather_df.loc[MG_Stations.Station]
Minas_Gerias = pd.DataFrame(MG)
Minas_Gerias['precip_mm'] = Minas_Gerias.precip * 1
MG_Count = Minas_Gerias.reset_index().station.nunique()
MG_Precip = (Minas_Gerias.precip.sum()/(MG_Count*precip_adjustment)).round(1)
MG_1_5_Day = ((Minas_Gerias[(Minas_Gerias.fhr<=120)].precip.sum())/((MG_Count*precip_adjustment))).round(1)
MG_6_10_Day = ((Minas_Gerias[(Minas_Gerias.fhr>120)&(Minas_Gerias.fhr<=240)].precip.sum())/((MG_Count*precip_adjustment))).round(1)
MG_11_15_Day = ((Minas_Gerias[(Minas_Gerias.fhr>240)].precip.sum())/((MG_Count*precip_adjustment))).round(1)
Minas_Gerias_precip_Forecast = Minas_Gerias.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Minas_Gerias_Forecast = Minas_Gerias_precip_Forecast.groupby(['Date']).mean()
Minas_Gerias_Forecast_Mean = Minas_Gerias.groupby(['Date', 'stations']).tmp2m.mean()
Minas_Gerias_Forecast_Mean_Temp = Minas_Gerias_Forecast_Mean.groupby(['Date']).mean()
Minas_Gerias_Forecast_Max = Minas_Gerias.groupby(['Date','stations']).tmp2m.max()
Minas_Gerias_Forecast_Max_Temp =Minas_Gerias_Forecast_Max.groupby(['Date']).mean()
Minas_Gerias_Forecast_Min = Minas_Gerias.groupby(['Date','stations']).tmp2m.min()
Minas_Gerias_Forecast_Min_Temp = Minas_Gerias_Forecast_Min.groupby(['Date']).mean()

MT= weather_df.loc[MT_Stations.Station]
Mato_Grosso = pd.DataFrame(MT)
Mato_Grosso['precip_mm'] = Mato_Grosso.precip * 1
MT_Count = Mato_Grosso.reset_index().station.nunique()
MT_Precip = (Mato_Grosso.precip.sum()/(MT_Count*precip_adjustment)).round(1)
MT_1_5_Day = ((Mato_Grosso[(Mato_Grosso.fhr<=120)].precip.sum())/((MT_Count*precip_adjustment))).round(1)
MT_6_10_Day = ((Mato_Grosso[(Mato_Grosso.fhr>120)&(Mato_Grosso.fhr<=240)].precip.sum())/((MT_Count*precip_adjustment))).round(1)
MT_11_15_Day = ((Mato_Grosso[(Mato_Grosso.fhr>240)].precip.sum())/((MT_Count*precip_adjustment))).round(1)
Mato_Grosso_precip_Forecast = Mato_Grosso.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Mato_Grosso_Forecast = Mato_Grosso_precip_Forecast.groupby(['Date']).mean()
Mato_Grosso_Forecast_Mean = Mato_Grosso.groupby(['Date', 'stations']).tmp2m.mean()
Mato_Grosso_Forecast_Mean_Temp = Mato_Grosso_Forecast_Mean.groupby(['Date']).mean()
Mato_Grosso_Forecast_Max = Mato_Grosso.groupby(['Date','stations']).tmp2m.max()
Mato_Grosso_Forecast_Max_Temp =Mato_Grosso_Forecast_Max.groupby(['Date']).mean()
Mato_Grosso_Forecast_Min = Mato_Grosso.groupby(['Date','stations']).tmp2m.min()
Mato_Grosso_Forecast_Min_Temp = Mato_Grosso_Forecast_Min.groupby(['Date']).mean()

MS= weather_df.loc[MS_Stations.Station]
Mato_Grosso_Sol = pd.DataFrame(MS)
Mato_Grosso_Sol['precip_mm'] = Mato_Grosso_Sol.precip * 1
MS_Count = Mato_Grosso_Sol.reset_index().station.nunique()
MS_Precip = (Mato_Grosso_Sol.precip.sum()/(MS_Count*precip_adjustment)).round(1)
MS_1_5_Day = ((Mato_Grosso_Sol[(Mato_Grosso_Sol.fhr<=120)].precip.sum())/((MS_Count*precip_adjustment))).round(1)
MS_6_10_Day = ((Mato_Grosso_Sol[(Mato_Grosso_Sol.fhr>120)&(Mato_Grosso_Sol.fhr<=240)].precip.sum())/((MS_Count*precip_adjustment))).round(1)
MS_11_15_Day = ((Mato_Grosso_Sol[(Mato_Grosso_Sol.fhr>240)].precip.sum())/((MS_Count*precip_adjustment))).round(1)
Mato_Grosso_Sol_precip_Forecast = Mato_Grosso_Sol.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Mato_Grosso_Sol_Forecast = Mato_Grosso_Sol_precip_Forecast.groupby(['Date']).mean()
Mato_Grosso_Sol_Forecast_Mean = Mato_Grosso_Sol.groupby(['Date', 'stations']).tmp2m.mean()
Mato_Grosso_Sol_Forecast_Mean_Temp = Mato_Grosso_Sol_Forecast_Mean.groupby(['Date']).mean()
Mato_Grosso_Sol_Forecast_Max = Mato_Grosso_Sol.groupby(['Date','stations']).tmp2m.max()
Mato_Grosso_Sol_Forecast_Max_Temp =Mato_Grosso_Sol_Forecast_Max.groupby(['Date']).mean()
Mato_Grosso_Sol_Forecast_Min = Mato_Grosso_Sol.groupby(['Date','stations']).tmp2m.min()
Mato_Grosso_Sol_Forecast_Min_Temp = Mato_Grosso_Sol_Forecast_Min.groupby(['Date']).mean()

RS = weather_df.loc[RS_Stations.Station]
RGDS = pd.DataFrame(RS)
RGDS['precip_mm'] = RGDS.precip * 1
RS_Count = RGDS.reset_index().station.nunique()
RS_Precip = (RGDS.precip.sum()/(RS_Count*precip_adjustment)).round(1)
RS_1_5_Day = ((RGDS[(RGDS.fhr<=120)].precip.sum())/((RS_Count*precip_adjustment))).round(1)
RS_6_10_Day = ((RGDS[(RGDS.fhr>120)&(RGDS.fhr<=240)].precip.sum())/((RS_Count*precip_adjustment))).round(1)
RS_11_15_Day = ((RGDS[(RGDS.fhr>240)].precip.sum())/((RS_Count*precip_adjustment))).round(1)
RGDS_precip_Forecast = RGDS.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
RGDS_Forecast = RGDS_precip_Forecast.groupby(['Date']).mean()
RGDS_Forecast_Mean = RGDS.groupby(['Date', 'stations']).tmp2m.mean()
RGDS_Forecast_Mean_Temp = RGDS_Forecast_Mean.groupby(['Date']).mean()
RGDS_Forecast_Max = RGDS.groupby(['Date','stations']).tmp2m.max()
RGDS_Forecast_Max_Temp =RGDS_Forecast_Max.groupby(['Date']).mean()
RGDS_Forecast_Min = RGDS.groupby(['Date','stations']).tmp2m.min()
RGDS_Forecast_Min_Temp = RGDS_Forecast_Min.groupby(['Date']).mean() 

PR= weather_df.loc[PR_Stations.Station]
Parana = pd.DataFrame(PR)
Parana['precip_mm'] = Parana.precip * 1
PR_Count = Parana.reset_index().station.nunique()
PR_Precip = (Parana.precip.sum()/(PR_Count*precip_adjustment)).round(1)
PR_1_5_Day = ((Parana[(Parana.fhr<=120)].precip.sum())/((PR_Count*precip_adjustment))).round(1)
PR_6_10_Day = ((Parana[(Parana.fhr>120)&(Parana.fhr<=240)].precip.sum())/((PR_Count*precip_adjustment))).round(1)
PR_11_15_Day = ((Parana[(Parana.fhr>240)].precip.sum())/((PR_Count*precip_adjustment))).round(1)
Parana_precip_Forecast = Parana.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Parana_Forecast = Parana_precip_Forecast.groupby(['Date']).mean()
Parana_Forecast_Mean = Parana.groupby(['Date', 'stations']).tmp2m.mean()
Parana_Forecast_Mean_Temp = Parana_Forecast_Mean.groupby(['Date']).mean()
Parana_Forecast_Max = Parana.groupby(['Date','stations']).tmp2m.max()
Parana_Forecast_Max_Temp =Parana_Forecast_Max.groupby(['Date']).mean()
Parana_Forecast_Min = Parana.groupby(['Date','stations']).tmp2m.min()
Parana_Forecast_Min_Temp = Parana_Forecast_Min.groupby(['Date']).mean() 

GO= weather_df.loc[GO_Stations.Station]
Goias = pd.DataFrame(GO)
Goias['precip_mm'] = Goias.precip * 1
GO_Count = Goias.reset_index().station.nunique()
GO_Precip = (Goias.precip.sum()/(GO_Count*precip_adjustment)).round(1)
GO_1_5_Day = ((Goias[(Goias.fhr<=120)].precip.sum())/((GO_Count*precip_adjustment))).round(1)
GO_6_10_Day = ((Goias[(Goias.fhr>120)&(Goias.fhr<=240)].precip.sum())/((GO_Count*precip_adjustment))).round(1)
GO_11_15_Day = ((Goias[(Goias.fhr>240)].precip.sum())/((GO_Count*precip_adjustment))).round(1)
Goias_precip_Forecast = Goias.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Goias_Forecast = Goias_precip_Forecast.groupby(['Date']).mean()
Goias_Forecast_Mean = Goias.groupby(['Date', 'stations']).tmp2m.mean()
Goias_Forecast_Mean_Temp = Goias_Forecast_Mean.groupby(['Date']).mean()
Goias_Forecast_Max = Goias.groupby(['Date','stations']).tmp2m.max()
Goias_Forecast_Max_Temp =Goias_Forecast_Max.groupby(['Date']).mean()
Goias_Forecast_Min = Goias.groupby(['Date','stations']).tmp2m.min()
Goias_Forecast_Min_Temp = Goias_Forecast_Min.groupby(['Date']).mean()
 
Cordoba= weather_df.loc[Cordoba_Arg_Stations.Station]
Cordoba_Argentina = pd.DataFrame(Cordoba)
Cordoba_Argentina['precip_mm'] = Cordoba_Argentina.precip * 1
Cordoba_Count = Cordoba_Argentina.reset_index().station.nunique()
Cordoba_Arg_Precip = (Cordoba_Argentina.precip.sum()/(Cordoba_Count*precip_adjustment)).round(1)
Cordoba_1_5_Day = ((Cordoba_Argentina[(Cordoba_Argentina.fhr<=120)].precip.sum())/((Cordoba_Count*precip_adjustment))).round(1)
Cordoba_6_10_Day = ((Cordoba_Argentina[(Cordoba_Argentina.fhr>120)&(Cordoba_Argentina.fhr<=240)].precip.sum())/((Cordoba_Count*precip_adjustment))).round(1)
Cordoba_11_15_Day = ((Cordoba_Argentina[(Cordoba_Argentina.fhr>240)].precip.sum())/((Cordoba_Count*precip_adjustment))).round(1)
Cordoba_precip_Forecast = Cordoba_Argentina.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Cordoba_Forecast = Cordoba_precip_Forecast.groupby(['Date']).mean()
Cordoba_Forecast_Mean = Cordoba_Argentina.groupby(['Date', 'stations']).tmp2m.mean()
Cordoba_Forecast_Mean_Temp = Cordoba_Forecast_Mean.groupby(['Date']).mean()
Cordoba_Forecast_Max = Cordoba_Argentina.groupby(['Date','stations']).tmp2m.max()
Cordoba_Forecast_Max_Temp =Cordoba_Forecast_Max.groupby(['Date']).mean()
Cordoba_Forecast_Min = Cordoba_Argentina.groupby(['Date','stations']).tmp2m.min()
Cordoba_Forecast_Min_Temp = Cordoba_Forecast_Min.groupby(['Date']).mean() 


Santa_Fe= weather_df.loc[Santa_Fe_Arg_Stations.Station]
Santa_Fe_Argentina = pd.DataFrame(Santa_Fe)
Santa_Fe_Argentina['precip_mm'] = Santa_Fe_Argentina.precip * 1
Santa_Fe_Count = Santa_Fe_Argentina.reset_index().station.nunique()
Santa_Fe_Arg_Precip = (Santa_Fe_Argentina.precip.sum()/(Santa_Fe_Count*precip_adjustment)).round(1)
Santa_Fe_1_5_Day = ((Santa_Fe_Argentina[(Santa_Fe_Argentina.fhr<=120)].precip.sum())/((Santa_Fe_Count*precip_adjustment))).round(1)
Santa_Fe_6_10_Day = ((Santa_Fe_Argentina[(Santa_Fe_Argentina.fhr>120)&(Santa_Fe_Argentina.fhr<=240)].precip.sum())/((Santa_Fe_Count*precip_adjustment))).round(1)
Santa_Fe_11_15_Day = ((Santa_Fe_Argentina[(Santa_Fe_Argentina.fhr>240)].precip.sum())/((Santa_Fe_Count*precip_adjustment))).round(1)
Santa_Fe_precip_Forecast = Santa_Fe_Argentina.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Santa_Fe_Forecast = Santa_Fe_precip_Forecast.groupby(['Date']).mean()
Santa_Fe_Forecast_Mean = Santa_Fe_Argentina.groupby(['Date', 'stations']).tmp2m.mean()
Santa_Fe_Forecast_Mean_Temp = Santa_Fe_Forecast_Mean.groupby(['Date']).mean()
Santa_Fe_Forecast_Max = Santa_Fe_Argentina.groupby(['Date','stations']).tmp2m.max()
Santa_Fe_Forecast_Max_Temp =Santa_Fe_Forecast_Max.groupby(['Date']).mean()
Santa_Fe_Forecast_Min = Santa_Fe_Argentina.groupby(['Date','stations']).tmp2m.min()
Santa_Fe_Forecast_Min_Temp = Santa_Fe_Forecast_Min.groupby(['Date']).mean() 


BA= weather_df.loc[BA_Arg_Stations.Station]
BA_Argentina = pd.DataFrame(BA)
BA_Argentina['precip_mm'] = BA_Argentina.precip * 1
BA_Count = BA_Argentina.reset_index().station.nunique()
BA_Arg_Precip = (BA_Argentina.precip.sum()/(BA_Count*precip_adjustment)).round(1)
BA_1_5_Day = ((BA_Argentina[(BA_Argentina.fhr<=120)].precip.sum())/((BA_Count*precip_adjustment))).round(1)
BA_6_10_Day = ((BA_Argentina[(BA_Argentina.fhr>120)&(BA_Argentina.fhr<=240)].precip.sum())/((BA_Count*precip_adjustment))).round(1)
BA_11_15_Day = ((BA_Argentina[(BA_Argentina.fhr>240)].precip.sum())/((BA_Count*precip_adjustment))).round(1)
BA_precip_Forecast = BA_Argentina.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
BA_Forecast = BA_precip_Forecast.groupby(['Date']).mean()
BA_Forecast_Mean = BA_Argentina.groupby(['Date', 'stations']).tmp2m.mean()
BA_Forecast_Mean_Temp = BA_Forecast_Mean.groupby(['Date']).mean()
BA_Forecast_Max = BA_Argentina.groupby(['Date','stations']).tmp2m.max()
BA_Forecast_Max_Temp =BA_Forecast_Max.groupby(['Date']).mean()
BA_Forecast_Min = BA_Argentina.groupby(['Date','stations']).tmp2m.min()
BA_Forecast_Min_Temp = BA_Forecast_Min.groupby(['Date']).mean() 
 
Entre_Rios= weather_df.loc[Entre_Rios_Arg_Stations.Station]
Entre_Rios_Argentina = pd.DataFrame(Entre_Rios)
Entre_Rios_Argentina['precip_mm'] = Entre_Rios_Argentina.precip * 1
Entre_Rios_Count = Entre_Rios_Argentina.reset_index().station.nunique()
Entre_Rios_Arg_Precip = (Entre_Rios_Argentina.precip.sum()/(Entre_Rios_Count*precip_adjustment)).round(1)
Entre_Rios_1_5_Day = ((Entre_Rios_Argentina[(Entre_Rios_Argentina.fhr<=120)].precip.sum())/((Entre_Rios_Count*precip_adjustment))).round(1)
Entre_Rios_6_10_Day = ((Entre_Rios_Argentina[(Entre_Rios_Argentina.fhr>120)&(Entre_Rios_Argentina.fhr<=240)].precip.sum())/((Entre_Rios_Count*precip_adjustment))).round(1)
Entre_Rios_11_15_Day = ((Entre_Rios_Argentina[(Entre_Rios_Argentina.fhr>240)].precip.sum())/((Entre_Rios_Count*precip_adjustment))).round(1)
Entre_Rios_precip_Forecast = Entre_Rios_Argentina.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Entre_Rios_Forecast = Entre_Rios_precip_Forecast.groupby(['Date']).mean()
Entre_Rios_Forecast_Mean = Entre_Rios_Argentina.groupby(['Date', 'stations']).tmp2m.mean()
Entre_Rios_Forecast_Mean_Temp = Entre_Rios_Forecast_Mean.groupby(['Date']).mean()
Entre_Rios_Forecast_Max = Entre_Rios_Argentina.groupby(['Date','stations']).tmp2m.max()
Entre_Rios_Forecast_Max_Temp =Entre_Rios_Forecast_Max.groupby(['Date']).mean()
Entre_Rios_Forecast_Min = Entre_Rios_Argentina.groupby(['Date','stations']).tmp2m.min()
Entre_Rios_Forecast_Min_Temp = Entre_Rios_Forecast_Min.groupby(['Date']).mean() 

La_Pampa= weather_df.loc[La_Pampa_Arg_Stations.Station]
La_Pampa_Argentina = pd.DataFrame(La_Pampa)
La_Pampa_Argentina['precip_mm'] = La_Pampa_Argentina.precip * 1
La_Pampa_Count = La_Pampa_Argentina.reset_index().station.nunique()
La_Pampa_Arg_Precip = (La_Pampa_Argentina.precip.sum()/(La_Pampa_Count*precip_adjustment)).round(1)
La_Pampa_1_5_Day = ((La_Pampa_Argentina[(La_Pampa_Argentina.fhr<=120)].precip.sum())/((La_Pampa_Count*precip_adjustment))).round(1)
La_Pampa_6_10_Day = ((La_Pampa_Argentina[(La_Pampa_Argentina.fhr>120)&(La_Pampa_Argentina.fhr<=240)].precip.sum())/((La_Pampa_Count*precip_adjustment))).round(1)
La_Pampa_11_15_Day = ((La_Pampa_Argentina[(La_Pampa_Argentina.fhr>240)].precip.sum())/((La_Pampa_Count*precip_adjustment))).round(1)
La_Pampa_precip_Forecast = La_Pampa_Argentina.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
La_Pampa_Forecast = La_Pampa_precip_Forecast.groupby(['Date']).mean()
La_Pampa_Forecast_Mean = La_Pampa_Argentina.groupby(['Date', 'stations']).tmp2m.mean()
La_Pampa_Forecast_Mean_Temp = La_Pampa_Forecast_Mean.groupby(['Date']).mean()
La_Pampa_Forecast_Max = La_Pampa_Argentina.groupby(['Date','stations']).tmp2m.max()
La_Pampa_Forecast_Max_Temp =La_Pampa_Forecast_Max.groupby(['Date']).mean()
La_Pampa_Forecast_Min = La_Pampa_Argentina.groupby(['Date','stations']).tmp2m.min()
La_Pampa_Forecast_Min_Temp = La_Pampa_Forecast_Min.groupby(['Date']).mean() 


Salta= weather_df.loc[Salta_Arg_Stations.Station]
Salta_Argentina = pd.DataFrame(Salta)
Salta_Argentina['precip_mm'] = Salta_Argentina.precip * 1
Salta_Count = Salta_Argentina.reset_index().station.nunique()
Salta_Arg_Precip = (Salta_Argentina.precip.sum()/(Salta_Count*precip_adjustment)).round(1)
Salta_1_5_Day = ((Salta_Argentina[(Salta_Argentina.fhr<=120)].precip.sum())/((Salta_Count*precip_adjustment))).round(1)
Salta_6_10_Day = ((Salta_Argentina[(Salta_Argentina.fhr>120)&(Salta_Argentina.fhr<=240)].precip.sum())/((Salta_Count*precip_adjustment))).round(1)
Salta_11_15_Day = ((Salta_Argentina[(Salta_Argentina.fhr>240)].precip.sum())/((Salta_Count*precip_adjustment))).round(1)
Salta_precip_Forecast = Salta_Argentina.groupby(['Date', 'stations']).precip_mm.sum()#/(WI_Count*precip_adjustment)
Salta_Forecast = Salta_precip_Forecast.groupby(['Date']).mean()
Salta_Forecast_Mean = Salta_Argentina.groupby(['Date', 'stations']).tmp2m.mean()
Salta_Forecast_Mean_Temp = Salta_Forecast_Mean.groupby(['Date']).mean()
Salta_Forecast_Max = Salta_Argentina.groupby(['Date','stations']).tmp2m.max()
Salta_Forecast_Max_Temp =Salta_Forecast_Max.groupby(['Date']).mean()
Salta_Forecast_Min = Salta_Argentina.groupby(['Date','stations']).tmp2m.min()
Salta_Forecast_Min_Temp = Salta_Forecast_Min.groupby(['Date']).mean() 

Argentina_Precip_Daily = (Cordoba_Forecast*.3 + Santa_Fe_Forecast*.28 + BA_Forecast*.255 + La_Pampa_Forecast * .08 + Entre_Rios_Forecast * .065 + Salta_Forecast * .02).round(1)
Argentina_Precip = (Cordoba_Arg_Precip*.3 + Santa_Fe_Arg_Precip*.28 + BA_Arg_Precip*.255 + La_Pampa_Arg_Precip * .08 + Entre_Rios_Arg_Precip * .065 + Salta_Arg_Precip * .02).round(1)
Argentina_Precip_1_5_Day = (Cordoba_1_5_Day*.3 + Santa_Fe_1_5_Day*.28 + BA_1_5_Day*.255 + La_Pampa_1_5_Day * .08 + Entre_Rios_1_5_Day * .065 + Salta_1_5_Day * .02).round(1)
Argentina_Precip_6_10_Day = (Cordoba_6_10_Day*.3 + Santa_Fe_6_10_Day*.28 + BA_6_10_Day*.255 + La_Pampa_6_10_Day * .08 + Entre_Rios_6_10_Day * .065 + Salta_6_10_Day * .02).round(1)
Argentina_Precip_11_15_Day = (Cordoba_11_15_Day*.3 + Santa_Fe_11_15_Day*.28 + BA_11_15_Day*.255 + La_Pampa_11_15_Day * .08 + Entre_Rios_11_15_Day * .065 + Salta_11_15_Day * .02).round(1)
Argentina_Mean_Temp = (Cordoba_Forecast_Mean_Temp*.3 + Santa_Fe_Forecast_Mean_Temp*.28 + BA_Forecast_Mean_Temp*.255 + La_Pampa_Forecast_Mean_Temp * .08 + Entre_Rios_Forecast_Mean_Temp * .065 + Salta_Forecast_Mean_Temp * .02).round(1)

print("Model run through {} hours".format(weather_df.fhr.max()))
print("")
print("Paraguay Weather")
print("")
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("Paraguay", Paraguay_Precip,Paraguay_1_5_Day,Paraguay_6_10_Day,Paraguay_11_15_Day, weather_model,h))
print("")
print("Uruguay Weather")
print("")
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("Uruguay", Uruguay_Precip,Uruguay_1_5_Day,Uruguay_6_10_Day,Uruguay_11_15_Day, weather_model,h))
print("")
print("Brazil Weather")
print("")
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("SP", SP_Precip,SP_1_5_Day,SP_6_10_Day,SP_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("MG", MG_Precip,MG_1_5_Day,MG_6_10_Day,MG_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("RS", RS_Precip,RS_1_5_Day,RS_6_10_Day,RS_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("PR", PR_Precip,PR_1_5_Day,PR_6_10_Day,PR_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("MT", MT_Precip,MT_1_5_Day,MT_6_10_Day,MT_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("MS", MS_Precip,MS_1_5_Day,MS_6_10_Day,MS_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("GO", GO_Precip,GO_1_5_Day,GO_6_10_Day,GO_11_15_Day, weather_model,h))
print("")
print("Argentina Weather")
print("")
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("Cordoba_Arg", Cordoba_Arg_Precip,Cordoba_1_5_Day,Cordoba_6_10_Day,Cordoba_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("Santa_Fe_Arg", Santa_Fe_Arg_Precip,Santa_Fe_1_5_Day,Santa_Fe_6_10_Day,Santa_Fe_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("BA_Arg", BA_Arg_Precip,BA_1_5_Day,BA_6_10_Day,BA_11_15_Day, weather_model,h))
print('{} is {} mm total, {} mm: 1-5 day, {} mm: 6-10 day, {} mm: 11-15 day, basis {} model {}z run'.format("Argentina_Weighted", Argentina_Precip,Argentina_Precip_1_5_Day,Argentina_Precip_6_10_Day,Argentina_Precip_11_15_Day, weather_model,h))
print("")
print("Argentina Daily Precip")
print(Argentina_Precip_Daily )
print(Argentina_Precip_Daily.sum())
print("")
print("")
print("Rio Grande do Sol Daily Precip")
print(RGDS_Forecast)
print(RGDS_Forecast.sum())
print("")
print("Parana Daily Precip")
print(Parana_Forecast)
print(Parana_Forecast.sum())
print("")

