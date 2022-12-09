import pandas as pd
import numpy as np

df = pd.DataFrame({'Date': pd.date_range('2017-10-16', pd.Timestamp.now().strftime("%Y-%m-%d"))})
df['High'] = 48.20001
df['Low'] = 48.20001
df['Open'] = 48.20001
df['Close'] = 48.20001
df['Volume'] = 48.20001
df['Adj Close'] = 48.20001

df.to_csv('cache/DRE.csv', index=False)

