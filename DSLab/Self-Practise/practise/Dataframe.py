import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))

# print(df.sort_index(axis=1, ascending=False))
# print(df.head())
df.columns = list("ABCDE")
print(df.loc[0,'A'])