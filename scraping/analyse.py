import pandas as pd
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('period')
parser.add_argument('id_')
parser.add_argument('--name', default='MarcoGorelli')
args = parser.parse_args()

dfs = []
for file in os.listdir('.'):
    if not file.endswith('.csv'):
        continue 
    period, id_, ts = file.split('_')
    if period != args.period or id_ != args.id_:
        continue
    ts = pd.Timestamp(ts.split('.')[0])
    df = pd.read_csv(file, index_col=0)[['position', 'teamName', 'performance', 'forecastRank', 'decisionRank', 'overallRank']]
    df = pd.concat(
        [df, pd.DataFrame(df['performance'].str.replace('\'', '"').apply(json.loads).tolist(), index=df.index)],
        axis=1,
    )
    df = df.drop(columns='performance').copy()
    df['date'] = ts
    dfs.append(df)
df = pd.concat(dfs)
df = df[df['teamName']==args.name].sort_values('date')
print(df)

