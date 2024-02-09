#step1

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

from datetime import datetime,date,time,timezone

df = pd.read_csv('covid-vaccination-doses-per-capita.csv')

print(df.info())

df['Date'] = pd.to_datetime(df['Day'])

df.set_index('Date',inplace=True)

df.drop(['Day'],axis=1,inplace=True)

print(df.head())

print(df['Entity'].unique())

#Step 2

covid_c = df.groupby(['Entity'])

for key,group in covid_c:
    print('+key:',key)
    print('+number:',len(group))
    print(group.head())
    print('\n')

total_df = covid_c.sum()
print(total_df.head())
