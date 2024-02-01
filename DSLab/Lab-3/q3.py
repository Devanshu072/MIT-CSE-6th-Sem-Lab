import numpy as np
 
# a)
 
list = [76.33 , 58.449 , 354.3781 , 1000.0]
a = np.array(list)
print(a , end = "\n\n")
 
# b)
 
tuple = (43, 276, 35, 544)
a = np.array(tuple)
print(a , end = "\n\n")
 
# c)
 
a = np.zeros((3, 4))
print(a , end = "\n\n")
 
# d)
 
a = np.arange(0, 20, 5)
print(a , end = "\n\n")
 
# e)
 
a = np.arange(12).reshape((3, 4))
print(a , end = "\n")
a = np.reshape(a , (2, 2, 3))
print(a , end = "\n\n")
a = np.arange(9.0).reshape((3, 3))
 
# f)
 
print("Full array Max = " , a.max() , " Min = " , a.min() , " Sum = " , a.sum())
print("Rowwise array Max = " , a.max(axis = 1) , " Min = " , a.min(axis = 1) , " Sum= " , a.sum(axis = 1))
print("Rowwise array Max = " , a.max(axis = 0) , " Min = " , a.min(axis = 0) , " Sum= " , a.sum(axis = 0))
