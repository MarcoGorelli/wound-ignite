import numpy as np
from precise.skatertools.data.equitylive import get_prices
import pandas as pd
from pprint import pprint
from precise.skaters.covariance.runemp import run_emp_pcov_d0


def m6_data(interval='d', n_dim=100, n_obs=300, last_date=None, cache_path=None):
    # constituents = pd.read_csv(
    #     'https://raw.githubusercontent.com/microprediction/m6/main/data/official/M6_Universe.csv')[:n_dim]
    # tickers = constituents['symbol'].values
    tickers = np.array(['ABBV', 'ACN', 'AEP', 'AIZ', 'ALLE', 'AMAT', 'AMP', 'AMZN', 'AVB',
       'AVY', 'AXP', 'BDX', 'BF-B', 'BMY', 'BR', 'CARR', 'CDW', 'CE',
       'CHTR', 'CNC', 'CNP', 'COP', 'CTAS', 'CZR', 'DG', 'DPZ', 'DRE',
       'DXC', 'FB', 'FTV', 'GOOG', 'GPC', 'HIG', 'HST', 'JPM', 'KR',
       'OGN', 'PG', 'PPL', 'PRU', 'PYPL', 'RE', 'ROL', 'ROST', 'UNH',
       'URI', 'V', 'VRSK', 'WRK', 'XOM', 'IVV', 'IWM', 'EWU', 'EWG',
       'EWL', 'EWQ', 'IEUS', 'EWJ', 'EWT', 'MCHI', 'INDA', 'EWY', 'EWA',
       'EWH', 'EWZ', 'EWC', 'IEMG', 'LQD', 'HYG', 'SHY', 'IEF', 'TLT',
       'SEGA.L', 'IEAA.L', 'HIGH.L', 'JPEA.L', 'IAU', 'SLV', 'GSG',
       'REET', 'ICLN', 'IXN', 'IGF', 'IUVL.L', 'IUMO.L', 'SPMV.L',
       'IEVL.L', 'IEFM.L', 'MVEU.L', 'XLK', 'XLF', 'XLV', 'XLE', 'XLY',
       'XLI', 'XLC', 'XLU', 'XLP', 'XLB', 'VXX'])
    if (interval=='m') and (n_obs>60):
        print('Too many obs, switching to daily ')
        interval = 'd'
    df = pd.DataFrame(columns=tickers)
    for ticker in tickers:
        closing_prices = get_prices(ticker=ticker, n_obs=n_obs+1, interval=interval, last_date=last_date, cache_path=cache_path)
        while len(closing_prices) < n_obs+1:
            closing_prices = list(closing_prices) + list(closing_prices)
        closing_prices = closing_prices[-n_obs:]
        df[ticker] = np.diff(np.log(closing_prices))
    return df


def m6_cov(f=None, interval='d', n_dim=100, n_obs=300, last_date=None, cache_path=None):
    """ Use any skater to estimate daily (by default) covariance
    :param f: cov skater
    :return:
    """
    if f is None:
        f = run_emp_pcov_d0
    df = m6_data(interval=interval, n_dim=n_dim, n_obs=n_obs, last_date=last_date, cache_path=cache_path)
    tickers = list(df.columns)

    s = {}
    # for each row
    for y in df.values:
        x_mean, x_cov, s = f(s=s, y=y)
    return pd.DataFrame(index=tickers, columns=tickers, data=x_cov)


def m6_corr(f=None, n_dim=100, interval='d',n_obs=300):
    from precise.skaters.covarianceutil.datafunctions import cov_to_corrcoef
    covdf = m6_cov(f=f, n_dim=n_dim, interval=interval, n_obs=n_obs)
    tickers = list(covdf.columns)
    corr = cov_to_corrcoef(covdf.values)
    dfc = pd.DataFrame(index=tickers, columns=tickers, data=corr)
    return dfc


if __name__=='__main__':
    from precise.skaters.covariance.ewaemp import ewa_emp_pcov_d0_r01 as f
    pprint(m6_corr(interval='d',n_dim=4,f=f))
