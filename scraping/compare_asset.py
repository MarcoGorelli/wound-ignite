"""
Download eod data from: ??? (fill in later)
https://eodhistoricaldata.com/api/eod/AMZN.US?api_token=62a0a2fa295466.26948824
"""

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

asset  = sys.argv[1]
latest = pd.read_csv(f'../../asset_prices/{asset}.csv').iloc[:-1]
latest['Date'] = pd.to_datetime(latest['Date'])

latest['m6'] = latest['Date'].map(df[df['symbol']==asset.split('.')[0]].set_index('date')['price'])
print(latest[(latest['Adjusted_close'] - latest['m6']).abs() > .1][['Date', 'Adjusted_close', 'm6']])

print(f'biggest diff: {(latest["Adjusted_close"] - latest["m6"]).abs().max()}')
