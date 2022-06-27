import pandas as pd

import pandas as pd
import glob
import os
import sys

dfs = []
for file in glob.glob('../../asset_prices/assets_m6*'):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])
    df['download_date'] = pd.Timestamp(pd.Timestamp(os.path.getmtime(file), unit='s').date())
    dfs.append(df)
df = pd.concat(dfs)
df = df.drop_duplicates(['symbol', 'date', 'download_date']).copy()

df = df[df['download_date']==df['download_date'].max()].copy()


yfinance = pd.read_csv('../../asset_prices/data_Adj Close.csv')
df_yf = yfinance.melt(id_vars=['Date'], value_name='price', var_name='symbol')
df_yf['Date'] = pd.to_datetime(df_yf['Date'])
df['yf_price'] = df.set_index(['date', 'symbol']).index.map(df_yf.set_index(['Date', 'symbol'])['price'])
df = df[df['date'] < df['download_date']].copy()
print(df[(df['price'] - df['yf_price']).abs()>.1])
