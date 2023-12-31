#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:55:49 2021

@author: Kerollyn
"""
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pyart

#filename= '/Users/Kerollyn/Documents/Proj.Pesquisa/Casos-TCC/29:10:2019/PEL191029080001.RAWZPZC'
#radar = pyart.io.read(filename)

filename= '/Users/Kerollyn/Documents/Proj.Pesquisa/Casos-TCC/11:01/Cópia de CGU-250--2021-01-11--22-20-23.mvol'
radar = pyart.aux_io.read_gamic(filename)
 
fig = plt.figure(figsize=(12,8))
projection = ccrs.Orthographic(
 central_longitude=radar.longitude['data'][0],
 central_latitude=radar.latitude['data'][0])
display = pyart.graph.RadarMapDisplay(radar)
ax = fig.add_subplot(111, projection=projection)

estados  = cfeature.NaturalEarthFeature( category='cultural', scale='10m',
                                       facecolor='none', name='admin_1_states_provinces' )
ax.add_feature( estados, linewidth=0.5, edgecolor='black' )

display.plot_ppi_map('reflectivity',0, vmin= 10, vmax=55., min_lon=-56, max_lon=-49, min_lat=-34, max_lat=-28,
                ax=ax, fig=fig, resolution='10m', cmap='pyart_NWSRef')

display.plot_range_rings([50,100,150,200])

plt.show()
