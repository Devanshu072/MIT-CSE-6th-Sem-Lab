import pandas as pd

data = {'Name': ['Devanshu', 'Gauri', 'Mangla'], 
'Height': [181, 155, 182], 
'Qualification': ['BTech', 'BTech', 'BTech']}

df = pd.DataFrame.from_dict(data)

addr_list = ['Ahmedabad', 'Bareilly', 'Balabgarh'] 
df['Address'] = addr_list

print(df.head())