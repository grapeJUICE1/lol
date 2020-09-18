import numpy as np

arr = np.array([
    [1 , 7 , 8 , 9 , 8 , 7] ,
    [2 , 4 , 5 , 9 , 4 , 2] ,
    ])

arr2 = arr.flatten()

arr3 = arr2.reshape(2 ,2 , 3)

m = np.matrix(arr)
m1 = np.matrix('3 2 5 ; 5 5 6; 6 8 9')
m2 = np.matrix('1 2 3 ; 4 5 6; 7 8 9')
m3 = m1 * m2

print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr2)
print(arr3)
print(m)
print(np.diagonal(m2))
print(m3)
