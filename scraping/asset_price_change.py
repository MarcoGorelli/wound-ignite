"""
download from https://m6competition.com/Assets
"""

import pandas as pd
import glob

dfs = []
for file in glob.glob('../../asset_prices/assets_m6*'):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])
    df['download_date'] = df['date'].max() + pd.Timedelta(days=1)
    dfs.append(df)
df = pd.concat(dfs)
df = df.drop_duplicates(['symbol', 'date', 'download_date']).copy()

df = df[df['date'].isin(df[df['download_date'].eq(df['download_date'].max())]['date'].unique())].copy()
df = df.sort_values('download_date').copy()
pivot = df.pivot_table(index=['symbol', 'date'], columns='download_date', values='price')
pivot['pct_change'] = pivot.pct_change(axis=1).iloc[:, -1]
pivot = pivot.sort_values(['pct_change', 'date']).copy()

changed = pivot[(pivot['pct_change']!= 0)&(pivot['pct_change'].notna())].reset_index()['symbol'].unique()

with pd.option_context('display.max_rows', None):
    print(pivot[pivot['pct_change']>0])
