import pandas as pd
import numpy as np

df_2 = pd.DataFrame({'x1': ['x1 1'], 'new_columns': 'ok'})
df = pd.read_csv(r'version_test.csv', encoding='cp1251', index_col=0)
df = df.replace(["^\s*$"], np.NaN, regex=True)
df.dropna(inplace=True)
df = df.rename(columns={'values     ': 'values'})
df = df.apply(lambda x: x.str.replace(',', '.'))
df = df.astype({"values": np.float64, "Корень": np.float64})
df = df.groupby(['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3', 'values']).sum()
df = df.reset_index(drop=False)
df = df.merge(df_2)

