import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('period')
parser.add_argument('id_')
parser.add_argument('--name', default='MarcoGorelli')
args = parser.parse_args()

if args.period == 'Quarter' and args.id_ == 'Q1':
    df = pd.read_csv('2022-06-02/raw_q1.csv', sep='\t', skiprows=12)
elif args.period == 'Quarter' and args.id_ == 'Q2':
    df = pd.read_csv('2022-06-02/raw_q2.csv', sep='\t', skiprows=12)
df['tmp'] = 1
df['tmp1'] = (df['tmp'].cumsum()-1)//3
df1 = df.select_dtypes('number').groupby('tmp1').max()
daf = pd.concat([df1, df.groupby('tmp1')['Position'].nth(1).to_frame().rename(columns={'Position': 'name'}), df.groupby('tmp1')['Position'].nth(0)], axis=1).iloc[:-1]

daf = pd.concat([daf, pd.DataFrame(daf['name'].str.split(' ', n=1).to_numpy().tolist(), columns=['teamId', 'teamName'])], axis=1)
daf = daf.drop(columns='name').copy()
daf = daf.rename(columns={
    'Position': 'position',
    'Overall Rank (OR)': 'forecasts',
    'Rank (Forecasts)': 'decisions',
    'Performance of Forecasts (RPS)': 'forecastRank',
    'Performance of Decisions (IR)': 'decisionRank',
    'Team': 'overallRank',
})
daf = daf[['position', 'teamName', 'forecastRank', 'decisionRank', 'overallRank', 'forecasts', 'decisions']]
daf['date'] = '2022-06-02'
print(daf[daf['teamName']==args.name])

