import numpy as np
import pandas as pd

data = pd.read_excel('German Credit_for_Week2.xlsx')
data.iloc[0,0] = 69
print(data)