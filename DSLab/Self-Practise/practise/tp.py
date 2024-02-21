import pandas as pd
import numpy as np

ser = pd.Series(np.random.rand(34))
# print(type(ser))
print(ser)

df = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
print(df.describe())

df[0][0] = "Devanshu"

# print(df)
# print(df.dtype)
print(df.sort_index(axis=1, ascending=False))