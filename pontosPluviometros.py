#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:46:41 2023

@author: Kerollyn
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.feature import ShapelyFeature
import cartopy.io.shapereader as shpreader


# locais (diretórios) dos dados
# shapefile do IBGE com os municípios do RS
municipios_RS_shp = '/Users/Kerollyn/Documents/Proj.Pesquisa/RS_Municipios_2021/RS_Municipios_2021.shp'
pontos = '/Users/Kerollyn/Documents/Proj.Pesquisa/latlon - Página1-2.csv'

main_var = 'id'

df = pd.read_csv(pontos)
 
plt.figure(figsize=(12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-50, -56, -33.7, -27], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(number_format='.1f', degree_symbol='',\
                                       dateline_direction_label=True)
lat_formatter = LatitudeFormatter(number_format='.1f', degree_symbol='')
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

shape_feature = ShapelyFeature(shpreader.Reader(municipios_RS_shp).geometries(),\
                                   ccrs.PlateCarree(), facecolor='none', edgecolor='k', linewidth=0.2)
ax.add_feature(shape_feature)


for index, row in df.iterrows():
    plt.text(row['lon'],row['lat'],row['id'])


# Add info from DataFrame
normalize = colors.Normalize(vmin=min(df[main_var]), vmax=max(df[main_var]))
cs = ax.scatter(df['lon'].values, df['lat'].values,\
                    c=df[main_var].values, cmap=plt.get_cmap('jet'),\
                transform=ccrs.PlateCarree(), marker='o', s=40)  
    

plt.show()