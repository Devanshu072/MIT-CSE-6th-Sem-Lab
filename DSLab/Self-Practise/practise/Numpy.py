import numpy as np

# myarr = np.array([3,6,7,8,9])
# print(myarr.dtype)  

ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
ar2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(listarray)

# print("sum of y is:" , + listarray.sum(axis=0))
# print("sum of x is", + listarray.sum(axis=1))

# print(listarray.T)

# listarray.flat

# for item in listarray.flat:
#     print(item)

# lspace = np.linspace(1,5,49)
# print(lspace)

# one = np.array([1,3,55,6,9])
# print(ar.argmax(axis=0))
# print(ar.argmin())
# print(ar.argsort())

# print(ar + ar2)
# print(ar * ar2)
# print(np.sqrt(ar))

# print(ar.sum())
# print(ar.max())
# print(ar.min())
# print(ar.sort())

# print(ar.dot(ar2))

D1 = np.vstack((ar,ar2))
D2 = np.hstack((ar,ar2))

print(D1)
print(D2)