# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:50:39 2020

@author: towns
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

''' Mato Grosso Data'''
state = 11
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_MT_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_MT_vhi= df_MT_vhi.iloc[:,:-1]

df_MT_vhi = df_MT_vhi.replace(-1, np.NaN)
df_MT_vhi = df_MT_vhi.interpolate()
df_MT_vhi['Years'] = df_MT_vhi.Year.copy()
df_MT_vhi.set_index('Year',inplace=True)

''' Alagoas Data'''

state = 2
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_AL_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_AL_vhi= df_AL_vhi.iloc[:,:-1]

df_AL_vhi = df_AL_vhi.replace(-1, np.NaN)
df_AL_vhi = df_AL_vhi.interpolate()
df_AL_vhi['Years'] = df_AL_vhi.Year.copy()
df_AL_vhi.set_index('Year',inplace=True)

''' Bahia Data'''

state = 5
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_BA_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_BA_vhi= df_BA_vhi.iloc[:,:-1]

df_BA_vhi = df_BA_vhi.replace(-1, np.NaN)
df_BA_vhi = df_BA_vhi.interpolate()
df_BA_vhi['Years'] = df_BA_vhi.Year.copy()
df_BA_vhi.set_index('Year',inplace=True)

''' Goias Data'''

state = 9
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_GO_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_GO_vhi= df_GO_vhi.iloc[:,:-1]

df_GO_vhi = df_GO_vhi.replace(-1, np.NaN)
df_GO_vhi = df_GO_vhi.interpolate()
df_GO_vhi['Years'] = df_GO_vhi.Year.copy()
df_GO_vhi.set_index('Year',inplace=True)

''' Mato Grosso do Sol Data'''

state = 12
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_MS_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_MS_vhi= df_MS_vhi.iloc[:,:-1]

df_MS_vhi = df_MS_vhi.replace(-1, np.NaN)
df_MS_vhi = df_MS_vhi.interpolate()
df_MS_vhi['Years'] = df_MS_vhi.Year.copy()
df_MS_vhi.set_index('Year',inplace=True)


''' Minas Gerias Data'''

state = 13
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_MG_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_MG_vhi= df_MG_vhi.iloc[:,:-1]

df_MG_vhi = df_MG_vhi.replace(-1, np.NaN)
df_MG_vhi = df_MG_vhi.interpolate()
df_MG_vhi['Years'] = df_MG_vhi.Year.copy()
df_MG_vhi.set_index('Year',inplace=True)

''' Parana Data'''

state = 16
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_PR_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_PR_vhi= df_PR_vhi.iloc[:,:-1]

df_PR_vhi = df_PR_vhi.replace(-1, np.NaN)
df_PR_vhi = df_PR_vhi.interpolate()
df_PR_vhi['Years'] = df_PR_vhi.Year.copy()
df_PR_vhi.set_index('Year',inplace=True)


''' Rio Grande do Sol Data'''

state = 21
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_RS_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_RS_vhi= df_RS_vhi.iloc[:,:-1]

df_RS_vhi = df_RS_vhi.replace(-1, np.NaN)
df_RS_vhi = df_RS_vhi.interpolate()
df_RS_vhi['Years'] = df_RS_vhi.Year.copy()
df_RS_vhi.set_index('Year',inplace=True)

''' Santa Catarina Data'''

state = 24
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_SC_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_SC_vhi= df_SC_vhi.iloc[:,:-1]

df_SC_vhi = df_SC_vhi.replace(-1, np.NaN)
df_SC_vhi = df_SC_vhi.interpolate()
df_SC_vhi['Years'] = df_SC_vhi.Year.copy()
df_SC_vhi.set_index('Year',inplace=True)

''' Sao Paulo Data'''

state = 24
country = 'BRA'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_SP_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_SP_vhi= df_SP_vhi.iloc[:,:-1]

df_SP_vhi = df_SP_vhi.replace(-1, np.NaN)
df_SP_vhi = df_SP_vhi.interpolate()
df_SP_vhi['Years'] = df_SP_vhi.Year.copy()
df_SP_vhi.set_index('Year',inplace=True)

#####################################################################################

'''Argentina Buenos Aires'''
state = 1
country = 'ARG'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_BA_ARG_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_BA_ARG_vhi= df_BA_ARG_vhi.iloc[:,:-1]

df_BA_ARG_vhi = df_BA_ARG_vhi.replace(-1, np.NaN)
df_BA_ARG_vhi = df_BA_ARG_vhi.interpolate()
df_BA_ARG_vhi['Years'] = df_BA_ARG_vhi.Year.copy()
df_BA_ARG_vhi.set_index('Year',inplace=True)

'''Argentina Cordoba'''
state = 6
country = 'ARG'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_CO_ARG_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_CO_ARG_vhi= df_CO_ARG_vhi.iloc[:,:-1]

df_CO_ARG_vhi = df_CO_ARG_vhi.replace(-1, np.NaN)
df_CO_ARG_vhi = df_CO_ARG_vhi.interpolate()
df_CO_ARG_vhi['Years'] = df_CO_ARG_vhi.Year.copy()
df_CO_ARG_vhi.set_index('Year',inplace=True)

'''Argentina Entre Rios'''
state = 8
country = 'ARG'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_ER_ARG_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_ER_ARG_vhi= df_ER_ARG_vhi.iloc[:,:-1]

df_ER_ARG_vhi = df_ER_ARG_vhi.replace(-1, np.NaN)
df_ER_ARG_vhi = df_ER_ARG_vhi.interpolate()
df_ER_ARG_vhi['Years'] = df_ER_ARG_vhi.Year.copy()
df_ER_ARG_vhi.set_index('Year',inplace=True)

'''Argentina La Pampa'''
state = 11
country = 'ARG'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_LP_ARG_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_LP_ARG_vhi= df_LP_ARG_vhi.iloc[:,:-1]

df_LP_ARG_vhi = df_LP_ARG_vhi.replace(-1, np.NaN)
df_LP_ARG_vhi = df_LP_ARG_vhi.interpolate()
df_LP_ARG_vhi['Years'] = df_LP_ARG_vhi.Year.copy()
df_LP_ARG_vhi.set_index('Year',inplace=True)

'''Argentina Santa Fe'''
state = 21
country = 'ARG'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_SF_ARG_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_SF_ARG_vhi= df_SF_ARG_vhi.iloc[:,:-1]

df_SF_ARG_vhi = df_SF_ARG_vhi.replace(-1, np.NaN)
df_SF_ARG_vhi = df_SF_ARG_vhi.interpolate()
df_SF_ARG_vhi['Years'] = df_SF_ARG_vhi.Year.copy()
df_SF_ARG_vhi.set_index('Year',inplace=True)


'''Paraguay San Pedro'''

state = 18
country = 'PRY'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_SP_PRY_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_SP_PRY_vhi= df_SP_PRY_vhi.iloc[:,:-1]

df_SP_PRY_vhi = df_SP_PRY_vhi.replace(-1, np.NaN)
df_SP_PRY_vhi = df_SP_PRY_vhi.interpolate()
df_SP_PRY_vhi['Years'] = df_SP_PRY_vhi.Year.copy()
df_SP_PRY_vhi.set_index('Year',inplace=True)
 

'''Paraguay Itapua'''

state = 13
country = 'PRY'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_IT_PRY_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_IT_PRY_vhi= df_IT_PRY_vhi.iloc[:,:-1]

df_IT_PRY_vhi = df_IT_PRY_vhi.replace(-1, np.NaN)
df_IT_PRY_vhi = df_IT_PRY_vhi.interpolate()
df_IT_PRY_vhi['Years'] = df_IT_PRY_vhi.Year.copy()
df_IT_PRY_vhi.set_index('Year',inplace=True)


'''Paraguay Alto Parana'''

state = 2
country = 'PRY'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns

df_AP_PRY_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_AP_PRY_vhi= df_AP_PRY_vhi.iloc[:,:-1]

df_AP_PRY_vhi = df_AP_PRY_vhi.replace(-1, np.NaN)
df_AP_PRY_vhi = df_AP_PRY_vhi.interpolate()
df_AP_PRY_vhi['Years'] = df_AP_PRY_vhi.Year.copy()
df_AP_PRY_vhi.set_index('Year',inplace=True)

 

'''Paraguay Caaguazu'''


state = 6
country = 'PRY'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_CA_PRY_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_CA_PRY_vhi= df_CA_PRY_vhi.iloc[:,:-1]
 
df_CA_PRY_vhi = df_CA_PRY_vhi.replace(-1, np.NaN)
df_CA_PRY_vhi = df_CA_PRY_vhi.interpolate()
df_CA_PRY_vhi['Years'] = df_CA_PRY_vhi.Year.copy()
df_CA_PRY_vhi.set_index('Year',inplace=True)
 

'''Paraguay Canindeyu''' 

state = 7
country = 'PRY'
year_end = 2022

path = pd.read_csv(f'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID={state}&country={country}&yearlyTag=Weekly&type=Mean&TagCropland=crop&year1=1982&year2={year_end}', skiprows=1)
df = path.reset_index()
df.columns
df_CU_PRY_vhi = df.rename(columns={'index':'Year', 'year':'Week', 'week':'SMN', 'SMN':'SMT', 'SMT':'VCI', 'VCI':'TCI', 'TCI':'VHI',})
df_CU_PRY_vhi= df_CU_PRY_vhi.iloc[:,:-1]
 
df_CU_PRY_vhi = df_CU_PRY_vhi.replace(-1, np.NaN)
df_CU_PRY_vhi = df_CU_PRY_vhi.interpolate()
df_CU_PRY_vhi['Years'] = df_CU_PRY_vhi.Year.copy()
df_CU_PRY_vhi.set_index('Year',inplace=True)


######################################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df_MT_vhi['vhi_MT_mean'] = df_MT_vhi.groupby('Week')['VHI'].transform(np.mean)
df_AL_vhi['vhi_AL_mean'] = df_AL_vhi.groupby('Week')['VHI'].transform(np.mean)
df_BA_vhi['vhi_BA_mean'] = df_BA_vhi.groupby('Week')['VHI'].transform(np.mean)
df_GO_vhi['vhi_GO_mean'] = df_GO_vhi.groupby('Week')['VHI'].transform(np.mean)
df_MS_vhi['vhi_MS_mean'] = df_MS_vhi.groupby('Week')['VHI'].transform(np.mean)
df_MG_vhi['vhi_MG_mean'] = df_MG_vhi.groupby('Week')['VHI'].transform(np.mean)
df_PR_vhi['vhi_PR_mean'] = df_PR_vhi.groupby('Week')['VHI'].transform(np.mean)
df_RS_vhi['vhi_RS_mean'] = df_RS_vhi.groupby('Week')['VHI'].transform(np.mean)
df_SC_vhi['vhi_SC_mean'] = df_SC_vhi.groupby('Week')['VHI'].transform(np.mean)
df_SP_vhi['vhi_SP_mean'] = df_SP_vhi.groupby('Week')['VHI'].transform(np.mean)

df_BA_ARG_vhi['vhi_ARG_BA_mean'] = df_BA_ARG_vhi.groupby('Week')['VHI'].transform(np.mean)
df_ER_ARG_vhi['vhi_ARG_ER_mean'] = df_ER_ARG_vhi.groupby('Week')['VHI'].transform(np.mean)
df_LP_ARG_vhi['vhi_ARG_LP_mean'] = df_LP_ARG_vhi.groupby('Week')['VHI'].transform(np.mean)
df_SF_ARG_vhi['vhi_ARG_SF_mean'] = df_SF_ARG_vhi.groupby('Week')['VHI'].transform(np.mean)
df_CO_ARG_vhi['vhi_ARG_CO_mean'] = df_CO_ARG_vhi.groupby('Week')['VHI'].transform(np.mean)

#Paraguay

df_SP_PRY_vhi['vhi_SP_PRY_mean'] = df_SP_PRY_vhi.groupby('Week')['VHI'].transform(np.mean)
df_IT_PRY_vhi['vhi_IT_PRY_mean'] = df_IT_PRY_vhi.groupby('Week')['VHI'].transform(np.mean)
df_AP_PRY_vhi['vhi_AP_PRY_mean'] = df_AP_PRY_vhi.groupby('Week')['VHI'].transform(np.mean)
df_CA_PRY_vhi['vhi_CA_PRY_mean'] = df_CA_PRY_vhi.groupby('Week')['VHI'].transform(np.mean)
df_CU_PRY_vhi['vhi_CU_PRY_mean'] = df_CU_PRY_vhi.groupby('Week')['VHI'].transform(np.mean)


#df_vhi['ARG_Total'] = (df_vhi.ARG_BA*.28 + df_vhi.ARG_SF*.34 + df_vhi.ARG_CO*.32 + df_vhi.ARG_ER*.05) 
#df_vhi['vhi_ARG_Total_mean'] = df_vhi.groupby('Week')['ARG_Total'].transform(np.mean)

df_MT_vhi['MT_vs_mean'] = df_MT_vhi.VHI - df_MT_vhi['vhi_MT_mean']
df_AL_vhi['AL_vs_mean'] = df_AL_vhi.VHI - df_AL_vhi['vhi_AL_mean']
df_BA_vhi['BA_vs_mean'] = df_BA_vhi.VHI - df_BA_vhi['vhi_BA_mean']
df_GO_vhi['GO_vs_mean'] = df_GO_vhi.VHI - df_GO_vhi['vhi_GO_mean']
df_MS_vhi['MS_vs_mean'] = df_MS_vhi.VHI - df_MS_vhi['vhi_MS_mean']
df_MG_vhi['MG_vs_mean'] = df_MG_vhi.VHI - df_MG_vhi['vhi_MG_mean']
df_PR_vhi['PR_vs_mean'] = df_PR_vhi.VHI - df_PR_vhi['vhi_PR_mean']
df_RS_vhi['RS_vs_mean'] = df_RS_vhi.VHI - df_RS_vhi['vhi_RS_mean']
df_SC_vhi['SC_vs_mean'] = df_SC_vhi.VHI - df_SC_vhi['vhi_SC_mean']
df_SP_vhi['SP_vs_mean'] = df_SP_vhi.VHI - df_SP_vhi['vhi_SP_mean']

#df_vhi['Brazil_vs_mean'] = df_vhi.MT_vs_mean + df_vhi.BA_vs_mean + df_vhi.GO_vs_mean + df_vhi.MS_vs_mean + df_vhi.MG_vs_mean + df_vhi.PR_vs_mean + df_vhi.RS_vs_mean
df_BA_ARG_vhi['ARG_BA_vs_mean'] = df_BA_ARG_vhi['VHI'] - df_BA_ARG_vhi['vhi_ARG_BA_mean'] 
df_ER_ARG_vhi['ARG_ER_vs_mean'] = df_ER_ARG_vhi['VHI'] - df_ER_ARG_vhi['vhi_ARG_ER_mean'] 
df_LP_ARG_vhi['ARG_LP_vs_mean'] = df_LP_ARG_vhi['VHI'] - df_LP_ARG_vhi['vhi_ARG_LP_mean'] 
df_SF_ARG_vhi['ARG_SF_vs_mean'] = df_SF_ARG_vhi['VHI'] - df_SF_ARG_vhi['vhi_ARG_SF_mean'] 
df_CO_ARG_vhi['ARG_CO_vs_mean'] = df_CO_ARG_vhi['VHI'] - df_CO_ARG_vhi['vhi_ARG_CO_mean'] 


df_SP_PRY_vhi['SP_PRY_vs_mean'] = df_SP_PRY_vhi['VHI'] - df_SP_PRY_vhi['vhi_SP_PRY_mean']
df_IT_PRY_vhi['IT_PRY_vs_mean'] = df_IT_PRY_vhi['VHI'] - df_IT_PRY_vhi['vhi_IT_PRY_mean']
df_AP_PRY_vhi['AP_PRY_vs_mean'] = df_AP_PRY_vhi['VHI'] - df_AP_PRY_vhi['vhi_AP_PRY_mean']
df_CA_PRY_vhi['CA_PRY_vs_mean'] = df_CA_PRY_vhi['VHI'] - df_CA_PRY_vhi['vhi_CA_PRY_mean']
df_CU_PRY_vhi['CU_PRY_vs_mean'] = df_CU_PRY_vhi['VHI'] - df_CU_PRY_vhi['vhi_CU_PRY_mean']
 

df_BA_ARG_vhi['ARG_vs_mean'] = df_BA_ARG_vhi['ARG_BA_vs_mean']*.25 + df_ER_ARG_vhi['ARG_ER_vs_mean'] *.05 + df_LP_ARG_vhi['ARG_LP_vs_mean']*.06 + df_SF_ARG_vhi['ARG_SF_vs_mean']*.32 + df_CO_ARG_vhi['ARG_CO_vs_mean']*.32
#df_vhi['Brazil_Safra_vs_mean'] = df_vhi.MT_vs_mean*.46 + df_vhi.PR_vs_mean*.2 + df_vhi.SP_vs_mean*.04 + df_vhi.MG_vs_mean*.03 + df_vhi.GO_vs_mean*.125 + df_vhi.MS_vs_mean*.145
df_SP_PRY_vhi['PRY_vs_mean'] = df_SP_PRY_vhi['SP_PRY_vs_mean']*.12  + df_IT_PRY_vhi['IT_PRY_vs_mean']*.21  +  df_AP_PRY_vhi['AP_PRY_vs_mean']*.16  +  df_CA_PRY_vhi['CA_PRY_vs_mean']*.29  +  df_CU_PRY_vhi['CU_PRY_vs_mean']*.22
df_SP_vhi['Brazil_Sugar_vs_mean'] = df_SP_vhi['SP_vs_mean']*.50 + df_PR_vhi['PR_vs_mean'] *.1 + df_MS_vhi['MS_vs_mean']*.1 + df_MG_vhi['MG_vs_mean']*.2 + df_GO_vhi['GO_vs_mean']*.1
df_SP_vhi['Brazil_Sugar_vs_mean'].plot()  
 
df_MT_vhi.MT_vs_mean.plot(legend = 'MT')
df_BA_vhi.BA_vs_mean.plot(legend = 'BA')
df_AL_vhi.AL_vs_mean.plot(legend = 'AL')
df_GO_vhi.GO_vs_mean.plot(legend = 'GO')
df_MS_vhi.MS_vs_mean.plot(legend = 'MS')
df_MG_vhi.MG_vs_mean.plot(legend = 'MG')
df_PR_vhi.PR_vs_mean.plot(legend = 'PR')
df_RS_vhi.RS_vs_mean.plot(legend = 'RS')
df_SC_vhi.SC_vs_mean.plot(legend = 'SC')
df_SP_vhi.SP_vs_mean.plot(legend = 'SP')

 

df_BA_ARG_vhi.ARG_BA_vs_mean.plot(legend = 'BA Arg.')
df_CO_ARG_vhi.ARG_CO_vs_mean.plot(legend = 'CO Arg.')
df_ER_ARG_vhi.ARG_ER_vs_mean.plot(legend = 'ER Arg.')
df_LP_ARG_vhi.ARG_LP_vs_mean.plot(legend = 'LP Arg.')
df_SF_ARG_vhi.ARG_SF_vs_mean.plot(legend = 'SF Arg.')
df_BA_ARG_vhi.ARG_vs_mean.plot(legend = 'Total Argentina')
 

df_BA_ARG_vhi.ARG_vs_mean.head(-20)
#df_vhi.ARG_vs_mean.groupby('Week')
  

df_SP_PRY_vhi['PRY_vs_mean'].plot(legend='Paraguay') 

c_w = 44 

 
arg = df_BA_ARG_vhi.groupby(['Week', 'Years'])['ARG_vs_mean'].sum()
arg[c_w].plot(kind='bar', figsize=(16, 10), title='ARG VHI vs MEAN')
 

MT = df_MT_vhi.groupby(['Week', 'Years'])['MT_vs_mean'].sum()
MT[c_w].plot(kind='bar') 

GO = df_GO_vhi.groupby(['Week', 'Years'])['GO_vs_mean'].sum()
GO[c_w].plot(kind='bar')
 

MG = df_MG_vhi.groupby(['Week', 'Years'])['MG_vs_mean'].sum()
MG[c_w].plot(kind='bar')

MS = df_MS_vhi.groupby(['Week', 'Years'])['MS_vs_mean'].sum()
MS[c_w].plot(kind='bar')

SP = df_SP_vhi.groupby(['Week', 'Years'])['SP_vs_mean'].sum()
SP[c_w].plot(kind='bar')

PR = df_PR_vhi.groupby(['Week', 'Years'])['PR_vs_mean'].sum()
PR[c_w].plot(kind='bar')
 
RS = df_RS_vhi.groupby(['Week', 'Years'])['RS_vs_mean'].sum()
RS[c_w].plot(kind='bar')

SC = df_SC_vhi.groupby(['Week', 'Years'])['SC_vs_mean'].sum()
SC[c_w].plot(kind='bar')

BA = df_BA_vhi.groupby(['Week', 'Years'])['BA_vs_mean'].sum()
BA[c_w].plot(kind='bar')

Paraguay = df_SP_PRY_vhi.groupby(['Week', 'Years'])['PRY_vs_mean'].sum()
Paraguay[c_w].plot(kind='bar')