"""
download from https://m6competition.com/Assets
"""

import pandas as pd
import glob
import os

dfs = []
for file in glob.glob('../../asset_prices/assets_m6*'):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])
    df['download_date'] = pd.Timestamp(pd.Timestamp(os.path.getmtime(file), unit='s').date())
    dfs.append(df)
df = pd.concat(dfs)
df = df.drop_duplicates(['symbol', 'date', 'download_date']).copy()

df = df[df['date'].isin(df[df['download_date'].eq(df['download_date'].max())]['date'].unique())].copy()
print(f'Latest date data has been downloaded for: {df["date"].max()}')
df = df.sort_values('download_date').copy()
pivot = df.pivot_table(index=['symbol', 'date'], columns='download_date', values='price')
pivot = pivot.sort_index(axis=1).copy()
pivot.columns = pivot.columns.strftime('%Y-%m-%d')
pivot = pivot.iloc[:, -2:].copy()
pivot['pct_change'] = pivot.pct_change(axis=1).iloc[:, -1]
pivot['max_change'] = pivot.reset_index().groupby('symbol')['pct_change'].transform(lambda x: max(x.abs())).to_numpy()
pivot = pivot.sort_values(['max_change', 'symbol', 'date']).copy()

changed = pivot[(pivot['pct_change']!= 0)&(pivot['pct_change'].notna())].reset_index()['symbol'].unique()

pivot = pivot.reset_index().copy().drop(columns='max_change')
pivot['date'] = pivot['date'].dt.strftime('%Y-%m-%d')
print('changed: ', changed)
with pd.option_context('display.max_rows', None):
    print(pivot[~pivot['pct_change'].eq(0)&pivot['pct_change'].notna()].to_markdown())

