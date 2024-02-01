X = [[100, 200],
[300, 400],
[500, 600]]
 
result = [[0,0,0],
 [0,0,0]]
 
print("Before Transpose: ")
print(X)
print()
 
print("After Transpose : ")
 
for i in range(len(X)): 
    for j in range(len(X[0])):
        result[j][i] = X[i][j]
        for r in result:
                print(result)