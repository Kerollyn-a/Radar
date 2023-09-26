#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:43:17 2023

@author: Kerollyn
"""
import matplotlib.pyplot as plt
import pyart

filename= '/Users/Kerollyn/Documents/Proj.Pesquisa/Casos-TCC/17:01:22/CGU-250--2022-01-17--19-10-23.mvol'
radar = pyart.aux_io.read_gamic(filename)

azimute = 40
secaoVertical = pyart.util.cross_section_ppi( radar, [azimute])
display = pyart.graph.RadarDisplay( secaoVertical )
display.plot( 'reflectivity', vmin=0, vmax=55. )
plt.show()