import pandas as pd
import numpy as np

dict1 = {
    "name":['harry', 'rohan', 'shubh'],
    "marks": [92,34,17],
    "city" : ['rampur', 'kolkata', 'bareilly']
}

df = pd.DataFrame(dict1)

# print(df.describe())

# df.to_csv('friends_index_false.csv', index= False)
# xyz = pd.read_csv('xyz.csv')
# print(xyz['148'][0])
# xyz[:3].index=['first', 'second', 'third']

friends = pd.read_csv('friends.csv')
friends.index=['first', 'second', 'third']
print(friends)