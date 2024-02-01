import numpy as np
#1. Array creation
A = np.array ([2,5,10])
print(A.dtype)
print()
#Will show, int64 data type
#____________________________#
B=np.array ([2.4,10.6,5.2])
print(B.dtype)
print()
#Will show, float64 data type
#____________________________#


A=np.array([(3,4,5),(12,6,1)])
print(A)
print()
Z=np.zeros((2,4),dtype=int) # will create zero matrix of dimension 2x4
print(Z)
print()



S=np.arange(10,30,5)
print(S) #will give (10,15,20,25,30), with step size of 5
print(np.arange( 0, 2, 0.3 )) # it accepts float arguments
print()


#lnstead of step-size, we can specify total number of elements in the array using
S1=np.linspace(0,2,9) # produce 9 numbers starting 0 & ends with 2array([ 0. , 0.25, 0.5 , 0.75, 1. , 1.25, 1.5 , 1.75, 2. ])
print(S1)