#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:26:28 2023

@author: Kerollyn
"""
import matplotlib.pyplot as plt
import pyart
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# locais (diretórios) dos dados
filename = '/Users/Kerollyn/Documents/Proj.Pesquisa/Casos-TCC/14:09/CGU-250--2021-09-14--00-00-23.mvol'

#Lendo dados
radar = pyart.aux_io.read_gamic(filename)

# inicializando objeto gráfico para o radar
display = pyart.graph.RadarMapDisplay( radar )

# definições gerais do gráfico
fig = plt.figure(figsize=(12,8))
projection = ccrs.Orthographic(
 central_longitude=radar.longitude['data'][0],
 central_latitude=radar.latitude['data'][0])
display = pyart.graph.RadarMapDisplay(radar)
ax = fig.add_subplot(111, projection=projection)

estados  = cfeature.NaturalEarthFeature( category='cultural', scale='10m',
                                       facecolor='none', name='admin_1_states_provinces' )
ax.add_feature( estados, linewidth=0.5, edgecolor='black' )

display.plot_ppi_map('reflectivity',1, vmin= 0., vmax=55., min_lon=-53.7, max_lon=-50, min_lat=-32.7, max_lat=-29.7,
                ax=ax, fig=fig, resolution='10m', cmap='pyart_NWSRef')


# adicionando pontos de interesse
display.plot_point(-52.317, -31.746,symbol='k*') #Areal - Pelotas
display.plot_point(-52.37, -31.75,symbol='k*') #Fragata  - Pelotas
display.plot_point(-52.342, -31.77,symbol='k*') #Centro - Pelotas
display.plot_point(-52.16, -31.69,symbol='k*') #Colonia z/3 - Pelotas
display.plot_point(-52.624, -31.46,symbol='k*') #Glória - Canguçu
display.plot_point(-52.897, -31.354,symbol='k*') #Santa clara - Canguçu
display.plot_point(-52.809, -31.403,symbol='k*') #Cochila dos  Cunha - Canguçu
display.plot_point(-52.743, -31.55,symbol='k*') #Tropeira - Canguçu
display.plot_point(-53.368, -32.558,symbol='k*') #Jaguarão
display.plot_point(-52.543, -30.55,symbol='k*') #Encruzilhada do sul
display.plot_point(-52.764, -31.764,symbol='k*') #Capão do Leão
#display.plot_point(-51.817, -30.851,symbol='k*') #Camaquã
display.plot_point(-52.802, -30.256,symbol='k*') #Cachoeira do Sul
display.plot_point(-52.802, -30.256,symbol='k*') #Capané - Cachoeira do Sul
display.plot_point(-52.867, -30.270,symbol='k*') #Vila jardim - Cachoeira do Sul
display.plot_point(-53.27, -30.338,symbol='k*') #Caçapava do Sul
display.plot_point(-52.826, -31.867,symbol='k*') #Pedro Osório
display.plot_point(-53.085, -32.238,symbol='k*') #Arroio Grande
display.plot_point(-52.158, -31.298,symbol='k*') #Interior - SLS
display.plot_point(-51.989, -31.369,symbol='k*') #Lomba - SLS
display.plot_point(-51.979, -31.369,symbol='k*') #Arroio SL - SLS


display.plot_point(radar.longitude["data"][0], radar.latitude["data"][0], symbol = 'wo')


plt.show()