import pandas as pd
import numpy as np
dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,6), index=dates, columns=list('ABCDEF'))
print(df[0:3])