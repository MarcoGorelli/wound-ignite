import pandas as pd
import numpy as np

files = ['examples_m6/full/march_submission_23_0.csv', 'examples_m6/full/march_submission_53_1.csv']

df0 = pd.read_csv(files[0])
df1 = pd.read_csv(files[1])
# df2 = pd.read_csv(files[2])

avg = 1/len(files)*df0.set_index('ID') + 1/len(files)*df1.set_index('ID')# + 1/len(files)*df2.set_index('ID')
avg.iloc[:, :5] = avg.iloc[:, :5] / avg.iloc[:, :5].sum(axis=1).to_numpy()[:, np.newaxis]
avg = avg.round(5)
print(avg.drop(columns='Decision').sum(axis=1).unique())
avg.reset_index().to_csv('examples_m6/full/march_submission_combined.csv', index=False)
