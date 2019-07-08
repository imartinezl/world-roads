#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:58:22 2019

@author: imartinez
"""
# %%
from pathlib import Path
import os
import geopandas as gpd
import matplotlib.pyplot as plt
import gc
from cartopy import crs as ccrs

fig, ax = plt.subplots(facecolor=('#181818'))
plt.tight_layout()

                                
#for filename in Path('data/processed').glob('**/rt_tramo_vial.shp'):
countries = ['NOR','SWE']
crs = ccrs.Orthographic(central_longitude=15, central_latitude=63)
crs_proj4 = crs.proj4_init

for c in countries:
	border_file = 'data/' + c + '_adm/' + c + '_adm0.shp'
	border = gpd.read_file( border_file).to_crs(crs_proj4)
	ax = border.plot(color='#000000', lw=1, alpha=1, ax=ax)
	filename = c + '_roads/gis_osm_roads_free_1.shp'
	print(filename, str(round(os.path.getsize(filename)/1e6,2))+ "MB")
	d = gpd.read_file( filename ).to_crs(crs_proj4)
	ax = d.plot(color='#00ffff', lw=0.5, alpha=0.1, ax=ax)
	ax = d.plot(color='#00ffff', lw=1, alpha=0.03, ax=ax)
	ax = d.plot(color='#00ffff', lw=2, alpha=0.015, ax=ax)
	gc.collect()


ax.set_xlim((-650000, 650000))
ax.set_ylim((-940000, 1000000))
ax.set_facecolor('#181818')
ax.axis('off')
ax.set_aspect('equal')   
plt.savefig('_'.join(countries) + '.png', facecolor=('#181818'), dpi=600 )


