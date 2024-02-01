import numpy as np
import pandas as pd
 
df = pd.DataFrame(np.array([[33, 25, 55], [90, 53, 86], [67, 48, 29]]))
#df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
 
print(df)
 
a = df.sum(axis = 0) #axis = 0 represents column
b = df.sum(axis = 1) #axis = 0 represents column
 
print("The column sum is :")
print(a)
 
print("The row sum is :")
print(b)