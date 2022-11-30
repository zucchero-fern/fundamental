# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 07:20:56 2022

@author: townsend.lansburg
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from datetime import datetime, timedelta
from dateutil import parser
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


'''Precip Input'''
df_Argentina = pd.read_excel("N://TJ//Weather//2022 SAM//Argentina_Soy_Weather_PRECIP_Data.xlsx", sheet_name = 'Pandas')

df_Argentina.columns
df_Argentina = df_Argentina.loc[df_Argentina["Year"] != 0]
df_Argentina = df_Argentina.dropna()
df_Argentina['DATETIME'] = df_Argentina.date.copy()
df_Argentina = df_Argentina.set_index('date')
df_Argentina.columns

corn_start = 340
corn_end = 70
soy_start = 191
soy_end = soy_start + 48
planting_start = 260
planting_end = planting_start +90
 
df_Argentina['Day_Year'] = pd.to_datetime(df_Argentina.DATETIME).dt.strftime("%j")
df_Argentina['Corn_Period'] = ((df_Argentina['Day_Year'].astype(int) >= corn_start) | (df_Argentina['Day_Year'].astype(int) <= corn_end))
df_Argentina['Planting_Period'] = ((df_Argentina['Day_Year'].astype(int) >= planting_start) & (df_Argentina['Day_Year'].astype(int) <= planting_end))
df_Argentina['Total_Daily_Precip_Mean'] = df_Argentina.groupby(['Month','Day'])['Total'].transform(np.mean)
df_Argentina['Santa_Fe_Daily_Precip_Mean'] = df_Argentina.groupby(['Month','Day'])['SantaFe'].transform(np.mean)
df_Argentina['Entre_Rios_Daily_Precip_Mean'] = df_Argentina.groupby(['Month','Day'])['EntreRios'].transform(np.mean)
df_Argentina['Cordoba_Daily_Precip_Mean'] = df_Argentina.groupby(['Month','Day'])['Cordoba'].transform(np.mean)
df_Argentina['BA_Daily_Precip_Mean'] = df_Argentina.groupby(['Month','Day'])['BA'].transform(np.mean)
df_Argentina['Salta_Daily_Precip_Mean'] = df_Argentina.groupby(['Month','Day'])['Salta'].transform(np.mean)



'''Temp Input'''
df_Argentina_temp = pd.read_excel("N://TJ//Weather//2022 SAM//Argentina_Soy_Weather_PRECIP_Data.xlsx", sheet_name = 'Pandas_Mean_Temp')

df_Argentina_temp.columns
df_Argentina_temp = df_Argentina_temp.loc[df_Argentina_temp["Year"] != 0]
df_Argentina_temp = df_Argentina_temp.dropna()
df_Argentina_temp['DATETIME'] = df_Argentina_temp.date.copy()
df_Argentina_temp = df_Argentina_temp.set_index('date')
df_Argentina_temp.columns

corn_start = 340
corn_end = 70
soy_start = 191
soy_end = soy_start + 48
planting_start = 260
planting_end = planting_start +90
 
df_Argentina_temp['Day_Year'] = pd.to_datetime(df_Argentina_temp.DATETIME).dt.strftime("%j")
df_Argentina_temp['Corn_Period'] = ((df_Argentina_temp['Day_Year'].astype(int) >= corn_start) | (df_Argentina_temp['Day_Year'].astype(int) <= corn_end))
df_Argentina_temp['Planting_Period'] = ((df_Argentina_temp['Day_Year'].astype(int) >= planting_start) & (df_Argentina_temp['Day_Year'].astype(int) <= planting_end))
df_Argentina_temp['Total_Daily_Mean_Temp'] = df_Argentina_temp.groupby(['Month','Day'])['Total'].transform(np.mean)
df_Argentina_temp['Santa_Fe_Daily_Mean_Temp'] = df_Argentina_temp.groupby(['Month','Day'])['SantaFe'].transform(np.mean)
df_Argentina_temp['Entre_Rios_Daily_Mean_Temp'] = df_Argentina_temp.groupby(['Month','Day'])['EntreRios'].transform(np.mean)
df_Argentina_temp['Cordoba_Daily_Mean_Temp'] = df_Argentina_temp.groupby(['Month','Day'])['Cordoba'].transform(np.mean)
df_Argentina_temp['BA_Daily_Mean_Temp'] = df_Argentina_temp.groupby(['Month','Day'])['BA'].transform(np.mean)
df_Argentina_temp['Salta_Daily_Mean_Temp'] = df_Argentina_temp.groupby(['Month','Day'])['Salta'].transform(np.mean)

from datetime import date

start_month = 11
start_day = 1
end_month = 10
end_day = 31

def Growing_Season(day):
    if pd.Timestamp(1987,start_month,start_day) <= day <= pd.Timestamp(1988,end_month, end_day):
        return '1987/1988'
    if pd.Timestamp(1988,start_month,start_day) <= day <= pd.Timestamp(1989,end_month, end_day):
        return '1988/1989'
    if pd.Timestamp(1989,start_month,start_day) <= day <= pd.Timestamp(1990,end_month, end_day):
        return '1989/1990'
    if pd.Timestamp(1991,start_month,start_day) <= day <= pd.Timestamp(1992,end_month, end_day):
        return '1991/1992'
    if pd.Timestamp(1993,start_month,start_day) <= day <= pd.Timestamp(1994,end_month, end_day):
        return '1993/1994'
    if pd.Timestamp(1994,start_month,start_day) <= day <= pd.Timestamp(1995,end_month, end_day):
        return '1994/1995'
    if pd.Timestamp(1995,start_month,start_day) <= day <= pd.Timestamp(1996,end_month, end_day):
        return '1995/1996'
    if pd.Timestamp(1996,start_month,start_day) <= day <= pd.Timestamp(1997,end_month, end_day):
        return '1996/1997'
    if pd.Timestamp(1997,start_month,start_day) <= day <= pd.Timestamp(1998,end_month, end_day):
        return '1997/1998'
    if pd.Timestamp(1998,start_month,start_day) <= day <= pd.Timestamp(1999,end_month, end_day):
        return '1998/1999'
    if pd.Timestamp(1999,start_month,start_day) <= day <= pd.Timestamp(2000,end_month, end_day):
        return '1999/2000'
    if pd.Timestamp(2000,start_month,start_day) <= day <= pd.Timestamp(2001,end_month, end_day):
        return '2000/2001'
    if pd.Timestamp(2001,start_month,start_day) <= day <= pd.Timestamp(2002,end_month, end_day):
        return '2001/2002'
    if pd.Timestamp(2002,start_month,start_day) <= day <= pd.Timestamp(2003,end_month, end_day):
        return '2002/2003'
    if pd.Timestamp(2003,start_month,start_day) <= day <= pd.Timestamp(2004,end_month, end_day):
        return '2003/2004'
    if pd.Timestamp(2004,start_month,start_day) <= day <= pd.Timestamp(2005,end_month, end_day):
        return '2004/2005'
    if pd.Timestamp(2005,start_month,start_day) <= day <= pd.Timestamp(2006,end_month, end_day):
        return '2005/2006'
    if pd.Timestamp(2006,start_month,start_day) <= day <= pd.Timestamp(2007,end_month, end_day):
        return '2006/2007'
    if pd.Timestamp(2007,start_month,start_day) <= day <= pd.Timestamp(2008,end_month, end_day):
        return '2007/2008'
    if pd.Timestamp(2008,start_month,start_day) <= day <= pd.Timestamp(2009,end_month, end_day):
        return '2008/2009'
    if pd.Timestamp(2009,start_month,start_day) <= day <= pd.Timestamp(2010,end_month, end_day):
        return '2009/2010'
    if pd.Timestamp(2010,start_month,start_day) <= day <= pd.Timestamp(2011,end_month, end_day):
        return '2010/2011'
    if pd.Timestamp(2011,start_month,start_day) <= day <= pd.Timestamp(2012,end_month, end_day):
        return '2011/2012'
    if pd.Timestamp(2012,start_month,start_day) <= day <= pd.Timestamp(2013,end_month, end_day):
        return '2012/2013'
    if pd.Timestamp(2013,start_month,start_day) <= day  <= pd.Timestamp(2014,end_month, end_day):
        return '2013/2014'
    if pd.Timestamp(2014,start_month,start_day) <= day  <= pd.Timestamp(2015,end_month, end_day):
        return '2014/2015'
    if pd.Timestamp(2015,start_month,start_day) <= day  <= pd.Timestamp(2016,end_month, end_day):
        return '2015/2016'
    if pd.Timestamp(2016,start_month,start_day) <= day  <= pd.Timestamp(2017,end_month, end_day):
        return '2016/2017'
    if pd.Timestamp(2017,start_month,start_day) <= day  <= pd.Timestamp(2018,end_month, end_day):
        return '2017/2018'
    if pd.Timestamp(2018,start_month,start_day) <= day  <= pd.Timestamp(2019,end_month, end_day):
        return '2018/2019'
    if pd.Timestamp(2019,start_month,start_day) <= day  <= pd.Timestamp(2020,end_month, end_day):
        return '2019/2020'
    if pd.Timestamp(2020,start_month,start_day) <= day  <= pd.Timestamp(2021,end_month, end_day):
        return '2020/2021'
    if pd.Timestamp(2021,start_month,start_day) <= day  <= pd.Timestamp(2022,end_month, end_day):
        return '2021/2022'
    if pd.Timestamp(2022,start_month,start_day) <= day  <= pd.Timestamp(2023,end_month, end_day):
        return '2022/2023'
    if pd.Timestamp(2023,start_month,start_day) <= day  <= pd.Timestamp(2024,end_month, end_day):
        return '2023/2024'
    if pd.Timestamp(2024,start_month,start_day) <= day  <= pd.Timestamp(2025,end_month, end_day):
        return '2024/2025'
    if pd.Timestamp(2025,start_month,start_day) <= day  <= pd.Timestamp(2026,end_month, end_day):
        return '2025/2026'
    
''''Precip'''

df_Argentina['Growing_Season'] = df_Argentina.DATETIME.apply(Growing_Season)

Total_precip_corn_period = df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Total'].sum()/df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Total_Daily_Precip_Mean'].sum()
Santa_Fe_precip_corn_period = df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['SantaFe'].sum()/df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Santa_Fe_Daily_Precip_Mean'].sum()
Entre_Rios_precip_corn_period = df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['EntreRios'].sum()/df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Entre_Rios_Daily_Precip_Mean'].sum()
Cordoba_precip_corn_period = df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Cordoba'].sum()/df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Cordoba_Daily_Precip_Mean'].sum()
BA_precip_corn_period = df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['BA'].sum()/df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['BA_Daily_Precip_Mean'].sum()
Salta_precip_corn_period = df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Salta'].sum()/df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Salta_Daily_Precip_Mean'].sum()



Total_precip_Planting_Period = df_Argentina.groupby(['Planting_Period', 'Year'])['Total'].sum()/df_Argentina.groupby(['Planting_Period', 'Year'])['Total_Daily_Precip_Mean'].sum()
Santa_Fe_precip_Planting_Period = df_Argentina.groupby(['Planting_Period', 'Year'])['SantaFe'].sum()/df_Argentina.groupby(['Planting_Period', 'Year'])['Santa_Fe_Daily_Precip_Mean'].sum()
Entre_Rios_precip_Planting_Period = df_Argentina.groupby(['Planting_Period', 'Year'])['EntreRios'].sum()/df_Argentina.groupby(['Planting_Period', 'Year'])['Entre_Rios_Daily_Precip_Mean'].sum()
Cordoba_precip_Planting_Period = df_Argentina.groupby(['Planting_Period', 'Year'])['Cordoba'].sum()/df_Argentina.groupby(['Planting_Period', 'Year'])['Cordoba_Daily_Precip_Mean'].sum()
BA_precip_Planting_Period = df_Argentina.groupby(['Planting_Period', 'Year'])['BA'].sum()/df_Argentina.groupby(['Planting_Period', 'Year'])['BA_Daily_Precip_Mean'].sum()
Salta_precip_Planting_Period = df_Argentina.groupby(['Planting_Period', 'Year'])['Salta'].sum()/df_Argentina.groupby(['Planting_Period', 'Year'])['Salta_Daily_Precip_Mean'].sum()


Total_precip_corn_period[True]
Total_precip_Planting_Period[True].plot(kind='bar')


#####################################################################################################################


''''Temp'''

df_Argentina_temp['Growing_Season'] = df_Argentina_temp.DATETIME.apply(Growing_Season)

Total_mean_temp_corn_period = df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Total'].sum()/df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Total_Daily_Mean_Temp'].sum()
Santa_Fe_mean_temp_corn_period = df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['SantaFe'].sum()/df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Santa_Fe_Daily_Mean_Temp'].sum()
Entre_Rios_mean_temp_corn_period = df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['EntreRios'].sum()/df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Entre_Rios_Daily_Mean_Temp'].sum()
Cordoba_mean_temp_corn_period = df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Cordoba'].sum()/df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Cordoba_Daily_Mean_Temp'].sum()
BA_mean_temp_corn_period = df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['BA'].sum()/df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['BA_Daily_Mean_Temp'].sum()
Salta_mean_temp_corn_period = df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Salta'].sum()/df_Argentina_temp.groupby(['Corn_Period', 'Growing_Season'])['Salta_Daily_Mean_Temp'].sum()



Total_mean_temp_Planting_Period = df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Total'].sum()/df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Total_Daily_Mean_Temp'].sum()
Santa_Fe_mean_temp_Planting_Period = df_Argentina_temp.groupby(['Planting_Period', 'Year'])['SantaFe'].sum()/df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Santa_Fe_Daily_Mean_Temp'].sum()
Entre_Rios_mean_temp_Planting_Period = df_Argentina_temp.groupby(['Planting_Period', 'Year'])['EntreRios'].sum()/df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Entre_Rios_Daily_Mean_Temp'].sum()
Cordoba_mean_temp_Planting_Period = df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Cordoba'].sum()/df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Cordoba_Daily_Mean_Temp'].sum()
BA_mean_temp_Planting_Period = df_Argentina_temp.groupby(['Planting_Period', 'Year'])['BA'].sum()/df_Argentina_temp.groupby(['Planting_Period', 'Year'])['BA_Daily_Mean_Temp'].sum()
Salta_mean_temp_Planting_Period = df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Salta'].sum()/df_Argentina_temp.groupby(['Planting_Period', 'Year'])['Salta_Daily_Mean_Temp'].sum()


Total_mean_temp_corn_period[True]
Total_mean_temp_Planting_Period[True].plot(kind='bar')


#######################################################################################################################


"""Anomoly Test"""
duration = len(Argentina_Precip_Daily)
start= -364
end = start+duration
print(weather_model, h,"z")
print("{} Day_Forecast_Precip_Anom".format(duration-1))
print("")

'''Planting Season'''
Argentina_accumulated_precip = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Total'].sum()[True])
Argentina_accumulated_precip_history = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Total_Daily_Precip_Mean'].sum()[True])
Argentina_pf = (Argentina_Precip_Daily.sum()+Argentina_accumulated_precip[-1])/(df_Argentina['Total_Daily_Precip_Mean'][start:end].sum()+Argentina_accumulated_precip_history[-1])

Cordoba_accumulated_precip = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Cordoba'].sum()[True])
Cordoba_accumulated_precip_history = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Cordoba_Daily_Precip_Mean'].sum()[True])
Cordoba_pf = (Cordoba_Forecast.sum()+Cordoba_accumulated_precip[-1])/(df_Argentina['Cordoba_Daily_Precip_Mean'][start:end].sum()+Cordoba_accumulated_precip_history[-1])

BA_accumulated_precip = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['BA'].sum()[True])
BA_accumulated_precip_history = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['BA_Daily_Precip_Mean'].sum()[True])
BA_pf = (BA_Forecast.sum()+BA_accumulated_precip[-1])/(df_Argentina['BA_Daily_Precip_Mean'][start:end].sum()+BA_accumulated_precip_history[-1])


Santa_Fe_accumulated_precip = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['SantaFe'].sum()[True])
Santa_Fe_accumulated_precip_history = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Santa_Fe_Daily_Precip_Mean'].sum()[True])
Santa_Fe_pf = (Santa_Fe_Forecast.sum()+Santa_Fe_accumulated_precip[-1])/(df_Argentina['Santa_Fe_Daily_Precip_Mean'][start:end].sum()+Santa_Fe_accumulated_precip_history[-1])

Entre_Rios_accumulated_precip = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['EntreRios'].sum()[True])
Entre_Rios_accumulated_precip_history = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Entre_Rios_Daily_Precip_Mean'].sum()[True])
Entre_Rios_pf = (Entre_Rios_Forecast.sum()+Entre_Rios_accumulated_precip[-1])/(df_Argentina['Entre_Rios_Daily_Precip_Mean'][start:end].sum()+Entre_Rios_accumulated_precip_history[-1])

Salta_accumulated_precip = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Salta'].sum()[True])
Salta_accumulated_precip_history = np.array(df_Argentina.groupby(['Planting_Period', 'Year'])['Salta_Daily_Precip_Mean'].sum()[True])
Salta_pf = (Salta_Forecast.sum()+Salta_accumulated_precip[-1])/(df_Argentina['Salta_Daily_Precip_Mean'][start:end].sum()+Salta_accumulated_precip_history[-1])


'''Growing Season'''
'''Need to start when the season begins, currently out of season'''
Argentina_accumulated_precip = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Total'].sum()[True])
Argentina_accumulated_precip_history = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Total_Daily_Precip_Mean'].sum()[True])
Argentina_pf = (Argentina_Precip_Daily.sum()+Argentina_accumulated_precip[-1])/(df_Argentina['Total_Daily_Precip_Mean'][start:end].sum()+Argentina_accumulated_precip_history[-1])

Cordoba_accumulated_precip = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Cordoba'].sum()[True])
Cordoba_accumulated_precip_history = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Cordoba_Daily_Precip_Mean'].sum()[True])
Cordoba_pf = (Cordoba_Forecast.sum()+Cordoba_accumulated_precip[-1])/(df_Argentina['Cordoba_Daily_Precip_Mean'][start:end].sum()+Cordoba_accumulated_precip_history[-1])

BA_accumulated_precip = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['BA'].sum()[True])
BA_accumulated_precip_history = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['BA_Daily_Precip_Mean'].sum()[True])
BA_pf = (BA_Forecast.sum()+BA_accumulated_precip[-1])/(df_Argentina['BA_Daily_Precip_Mean'][start:end].sum()+BA_accumulated_precip_history[-1])


Santa_Fe_accumulated_precip = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['SantaFe'].sum()[True])
Santa_Fe_accumulated_precip_history = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Santa_Fe_Daily_Precip_Mean'].sum()[True])
Santa_Fe_pf = (Santa_Fe_Forecast.sum()+Santa_Fe_accumulated_precip[-1])/(df_Argentina['Santa_Fe_Daily_Precip_Mean'][start:end].sum()+Santa_Fe_accumulated_precip_history[-1])

Entre_Rios_accumulated_precip = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['EntreRios'].sum()[True])
Entre_Rios_accumulated_precip_history = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Entre_Rios_Daily_Precip_Mean'].sum()[True])
Entre_Rios_pf = (Entre_Rios_Forecast.sum()+Entre_Rios_accumulated_precip[-1])/(df_Argentina['Entre_Rios_Daily_Precip_Mean'][start:end].sum()+Entre_Rios_accumulated_precip_history[-1])

Salta_accumulated_precip = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Salta'].sum()[True])
Salta_accumulated_precip_history = np.array(df_Argentina.groupby(['Corn_Period', 'Growing_Season'])['Salta_Daily_Precip_Mean'].sum()[True])
Salta_pf = (Salta_Forecast.sum()+Salta_accumulated_precip[-1])/(df_Argentina['Salta_Daily_Precip_Mean'][start:end].sum()+Salta_accumulated_precip_history[-1])





########################################################################################################################## 
#This bumps up or down historical average
'''Growing Season forecast with normal weather rest of season'''
bias_precip = 1
current_season = '2022/2023'
historical_season = '2021/2022'

normal_weather_test = (df_Argentina.loc[(df_Argentina['Growing_Season'] == historical_season) & (df_Argentina['Corn_Period'] == True)])
current_weather_test = (df_Argentina.loc[(df_Argentina['Growing_Season'] == current_season) & (df_Argentina['Corn_Period'] == True)])

'''Total_Argentina'''
forecast = Argentina_Precip_Daily
y =len(normal_weather_test)
w =len(current_weather_test) + len(forecast)


def cutoff(days):
    if y-w > len(forecast):
        return len(forecast)
    else:
        return y-w
#print(cutoff(y-w))

t = cutoff(y-w)


Normal_Total_Argentina_pf = (current_weather_test['Total'].sum() + normal_weather_test['Total_Daily_Precip_Mean'][w:].sum()*bias_precip + Argentina_Precip_Daily[:t].sum())/(normal_weather_test['Total_Daily_Precip_Mean'].sum())



'''BA_Argentina'''
#forecast = BA_Forecast
Normal_BA_Argentina_pf = (current_weather_test['BA'].sum() + normal_weather_test['BA_Daily_Precip_Mean'][w:].sum()*bias_precip + BA_Forecast[:t].sum())/(normal_weather_test['BA_Daily_Precip_Mean'].sum())

'''Santa_Fe_Argentina'''
#forecast = Santa_Fe_Forecast
Normal_SF_Argentina_pf = (current_weather_test['SantaFe'].sum() + normal_weather_test['Santa_Fe_Daily_Precip_Mean'][w:].sum()*bias_precip + Santa_Fe_Forecast[:t].sum())/(normal_weather_test['Santa_Fe_Daily_Precip_Mean'].sum())

'''Cordoba_Argentina'''
#forecast = Cordoba_Forecast
Normal_CO_Argentina_pf = (current_weather_test['Cordoba'].sum() + normal_weather_test['Cordoba_Daily_Precip_Mean'][w:].sum()*bias_precip + Cordoba_Forecast[:t].sum())/(normal_weather_test['Cordoba_Daily_Precip_Mean'].sum())



######################################################################################################################################

'''Planting Season with normal weather to end season'''
bias_precip = 1
current_season = 2022
historical_season = 2021


normal_weather_test = (df_Argentina.loc[(df_Argentina['Planting_Period'] == True) & (df_Argentina['Year'] == historical_season)])
current_weather_test = (df_Argentina.loc[(df_Argentina['Planting_Period'] == True) & (df_Argentina['Year'] == current_season)])

'''Total_Argentina'''
forecast = Argentina_Precip_Daily
y =len(normal_weather_test)
w =len(current_weather_test) + len(forecast)


def cutoff(days):
    if y-w > len(forecast):
        return len(forecast)
    else:
        return y-w
#print(cutoff(y-w))

t = cutoff(y-w)


Normal_Planting_Total_Argentina_pf = (current_weather_test['Total'].sum() + normal_weather_test['Total_Daily_Precip_Mean'][w:].sum()*bias_precip + Argentina_Precip_Daily[:t].sum())/(normal_weather_test['Total_Daily_Precip_Mean'].sum())



'''BA_Argentina'''
forecast = BA_Forecast
Normal_Planting_BA_Argentina_pf = (current_weather_test['BA'].sum() + normal_weather_test['BA_Daily_Precip_Mean'][w:].sum()*bias_precip + BA_Forecast[:t].sum())/(normal_weather_test['BA_Daily_Precip_Mean'].sum())

'''Santa_Fe_Argentina'''
forecast = Santa_Fe_Forecast
Normal_Planting_SF_Argentina_pf = (current_weather_test['SantaFe'].sum() + normal_weather_test['Santa_Fe_Daily_Precip_Mean'][w:].sum()*bias_precip + Santa_Fe_Forecast[:t].sum())/(normal_weather_test['Santa_Fe_Daily_Precip_Mean'].sum())

'''Cordoba_Argentina'''
forecast = Cordoba_Forecast
Normal_Planting_CO_Argentina_pf = (current_weather_test['Cordoba'].sum() + normal_weather_test['Cordoba_Daily_Precip_Mean'][w:].sum()*bias_precip + Cordoba_Forecast[:t].sum())/(normal_weather_test['Cordoba_Daily_Precip_Mean'].sum())







