#!/usr/bin/python3

import pandas as pd
import geopandas as gpd

df_states = gpd.read_file("https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_20m.zip")
df_states.to_crs(epsg=2163)
df_states.to_file("states.json", driver="GeoJSON")

