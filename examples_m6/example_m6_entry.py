from precise.skatertools.m6.competition import m6_competition_entry, m6_dump
from precise.whereami import M6_EXAMPLES
import os
import time
import json
import argparse
import pandas as pd

from precise.skaters.covariance.allcovskaters import ALL_COV_SKATERS
from precise.skaters.portfoliostatic.allstaticport import  PORT

# Example of creating an M6 Competition entry using random choice of cov estimation and port construction


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('f')
    parser.add_argument('port')
    args = parser.parse_args()
    kwargs = dict(
        f = args.f,
        port = args.port,
    )
    for last_date in ('2021-12-06', '2022-01-06', '2022-02-06'):
        df = m6_competition_entry(f=ALL_COV_SKATERS[kwargs['f']], port=PORT[kwargs['port']], last_date=last_date)
        name = f'{json.dumps(kwargs)}_{last_date}.csv'
        timestamped_csv_file = os.path.join(M6_EXAMPLES,'full',name)
        m6_dump(df=df,file_name=timestamped_csv_file)
