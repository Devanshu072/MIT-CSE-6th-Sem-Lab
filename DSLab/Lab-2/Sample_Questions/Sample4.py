import pandas as pd
import numpy as np
df1=pd.DataFrame({'A':pd.Timestamp('20130102'),'B':np.array([3]*4,dtype='int32'),
'C':pd.Categorical(['Male','Female','Male','Female'])})

print (df1)

df1.shape
(4,3)
df1.dtypes
dtype: object
df1.head()
#will display first 5 records
df1.tail()
#will display last 5 records
print(df1.summary())