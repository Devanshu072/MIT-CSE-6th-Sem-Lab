import pandas as pd

data = {'Name': ['Devanshu', 'Gauri', 'Mangla'], 
'Height': [181, 180, 179], 
'Qualification': ['BTech', 'MS', 'PhD']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
 
# Using DataFrame.insert() to add a column
df.insert(2, "Age", [21, 23, 24], True)

print(df)