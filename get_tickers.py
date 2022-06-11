import pandas as pd

constituents = pd.read_csv(
    'https://raw.githubusercontent.com/Mcompetitions/M6-methods/main/assets_m6.csv')
tickers = constituents['symbol'].unique().to_numpy().reshape(20, 5)
print(tickers.tolist())