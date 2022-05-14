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
f = 46
port = 14

if __name__=='__main__':
    df = m6_competition_entry(f=ALL_D0_SKATERS[f], port=PORT[port], last_date=pd.Timestamp.now(), cache_path=cache_path, scale_w=1/.25)
