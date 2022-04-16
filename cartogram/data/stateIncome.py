#!/usr/bin/python3

import pandas as pd

df = pd.read_csv("Census_Population.csv")

df2 = df[df['Label (Grouping)'] == '            Mean earnings (dollars)']

df3 = df2.filter(regex='!!Total!!Estimate').dropna(axis=1)
newcols = [col.replace('!!Total!!Estimate', '') for col in df3.columns]
df3.columns = newcols
df4 = df3.apply(lambda x: x.astype(str).str.replace(',','').apply(pd.to_numeric))

df4.to_csv("stateIncome.csv", index=False)
df4.to_json("stateIncome.json", orient='records')

