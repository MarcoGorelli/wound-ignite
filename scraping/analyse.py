import pandas as pd
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('period')
parser.add_argument('id_')
parser.add_argument('--name', default='MarcoGorelli')
parser.add_argument('--date', required=False)
parser.add_argument('--sort', required=False, default='position')
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

if args.date is not None:
    print(df[df['date']==args.date].sort_values(args.sort).head(10))    
else:
    print(df[df['teamName'].str.startswith(args.name)].sort_values('date'))

