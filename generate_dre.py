import pandas as pd
import numpy as np

df = pd.DataFrame({'Date': pd.date_range('2017-10-16', pd.Timestamp.now().strftime("%Y-%m-%d"))})
df['High'] = np.random.randn(len(df))
df['Low'] = np.random.randn(len(df))
df['Open'] = np.random.randn(len(df))
df['Close'] = np.random.randn(len(df))
df['Volume'] = np.random.randn(len(df))
df['Adj Close'] = np.random.randn(len(df))

df.to_csv('cache/DRE.csv', index=False)

