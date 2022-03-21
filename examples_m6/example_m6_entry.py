from precise.skatertools.m6.competition import m6_competition_entry, m6_dump
from precise.whereami import M6_EXAMPLES
import os
import time
import json
import argparse
import pandas as pd

from precise.skaters.covariance.allcovskaters import ALL_D0_SKATERS
from precise.skaters.portfoliostatic.allstaticport import  PORT

# Example of creating an M6 Competition entry using random choice of cov estimation and port construction

cache_path = 'cache'
f = 0
port = 0

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--f', type=int)
    args = parser.parse_args()
    df = m6_competition_entry(f=ALL_D0_SKATERS[f], port=PORT[port], last_date='2022-03-06', cache_path=cache_path)
    name = f'march_submission_{f}_{port}.csv'
    timestamped_csv_file = os.path.join(M6_EXAMPLES,'full',name)
    # m6_dump(df=df,file_name=timestamped_csv_file)
