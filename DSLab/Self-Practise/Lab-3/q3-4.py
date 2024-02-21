import numpy as np

#list se bana hua array
A = np.array([1.2,2.3,3.4,4.5,5.6,6.7])
print(A)

#tuple se bana hua array
B = np.array((1,2,3,4,5,6))
print(B)


C = np.zeros((3,4))
print(C)

#step of 5
D = np.arange(0,20,5)
print(D)
E = C.reshape((2,2,3))
print(E)
F = np.arange(0,15).reshape((3,5))
print(F)

for row in F:
    print(row)
    print("Max : ",max(row))
    print("Min : ",min(row))
    print("Sum : ",sum(row))
    
F = F.T

for col in F:
    print(col)
    print("Max : ",max(col))
    print("Min : ",min(col))
    print("Sum : ",sum(col))