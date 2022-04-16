#!/usr/bin/python3

import pandas as pd

df = pd.read_csv("Census_Population.csv")

# Get the mean income data
df2 = df[df['Label (Grouping)'] == '            Mean earnings (dollars)']

# Make column names reasonable
df3 = df2.filter(regex='!!Total!!Estimate').fillna(0)
newcols = [col.replace('!!Total!!Estimate', '') for col in df3.columns]
df3.columns = newcols
df4 = df3.apply(lambda x: x.astype(str).str.replace(',','').apply(pd.to_numeric, downcast='integer'))

# Write the data out to CSV for use by our D3JS code
df4.to_csv("stateIncome.csv", index=False)
#df4.to_json("stateIncome.json", orient='records')

# Create a version of the income data for use by QGIS
# Specifically this puts the data in rows instead of columns
df4["id"] = df4.index
df5 = df4.melt(id_vars=["id"], var_name="State", value_name="Income")
df5.drop(columns="id",inplace=True)
df5.to_csv("stateIncome2.csv")

