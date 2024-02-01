X = [[234,53,923],
[45, 432, 545],
[35, 724, 924]]
 
Y = [[540,814,121],
[68,247,453],
[435,365,925]]
 
result = [[0,0,0],
[0,0,0],
[0,0,0]]
 
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)