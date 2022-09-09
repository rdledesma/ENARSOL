#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 08:53:37 2022

@author: dario
"""

import pandas as pd
import Geo
import pvlib as pv

geo = Geo.Geo(freq='1', lat=-23.5839, long=-64.5068, gmt=-3, alt=1239, beta=0).df

df = pd.read_csv('EEA_Yuto_31082021_1236-489.csv', usecols=['fechaHora', 'global_wm2', 'directa_wm2', 'difusa_wm2'])

df['fechaHora'] = pd.to_datetime(df.fechaHora)

df['Y'] = df.fechaHora.dt.year
df['M'] = df.fechaHora.dt.month
df['J'] = df.fechaHora.dt.day_of_year

df = (df.set_index('fechaHora')
      .reindex(pd.date_range('2016-09-09','2018-12-31 23:59:00', freq='1 min'))
      .rename_axis(['fechaHora'])
      .fillna(0)
      .reset_index())


geo = Geo.Geo(freq='1', lat=-23.5839, long=-64.5068, gmt=-3, alt=1239, beta=0).df
import math 
df['CTZ'] = geo.CTZ
df['TOA'] = geo.TOA
df['TZ'] =  geo.CTZ.apply(math.degrees)
df_2016 = df[df.Y == 2016]
df_2016['CTZ'] = df_2016.CTZ
df_2016 = df_2016[df_2016.CTZ>0]


df_2017 = df[df.Y == 2017]
df_2017['CTZ'] = df_2017.CTZ
df_2017 = df_2017[df_2017.CTZ>0]

df_2018 = df[df.Y == 2018]
df_2018['CTZ'] = df_2018.CTZ
df_2018 = df_2018[df_2018.CTZ>0]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(facecolor='white')
plt.style.use('default')
ax.scatter(df_2017['CTZ'], df_2017.global_wm2, s=0.1)
plt.show()

1
location = pv.location.Location(latitude=-23.5839, longitude=-64.5068, tz="America/Argentina/Salta")
solar_position = location.get_solarposition(df.fechaHora)




