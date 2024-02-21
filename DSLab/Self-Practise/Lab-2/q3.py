import pandas as pd

students={"Name":["Devanshu","Gauri"],"Height":["5.9ft","Bohot chhoti"],"Qualification":["Student","Student"]}
df=pd.DataFrame(students)
print(df)
print("after adding address")
address=["Ahmedabad","Bareilly"]
df["Address"]=address
print(df)