import numpy as np
# from array import *
#
# arr = array('i' , [1,4,5,6,67,7])
#
# print(arr)


arr1 = np.array([1 , 3 , 4 ,5 ,6] ,int)
arr2 = np.linspace(0 ,16 )
arr3 = np.arange(0 , 15 , 2)
arr4 = np.logspace(1 , 40 , 5)
arr5 = np.zeros(7 , int)
arr6 = np.ones(7 , int)

print(arr1 , arr1.dtype)
print(arr2 , arr2.dtype)
print(arr3 , arr3.dtype)
print(arr4 ,'%.2f' %arr4[0] , '%.2f' %arr4[4], arr4.dtype)
print(arr5 , arr5.dtype)
print(arr6 , arr6.dtype)

print(np.max(arr1) , np.min(arr1))
print(np.sin(arr1) , np.cos(arr1) , np.log(arr1) , np.tan(arr1))
print(np.concatenate([arr1 , arr5]))


# for i in range(0 , max) :
#     index = arr1.tolist().index(i)
#     arr1[index] = i * 5
#
# print(np.sort(arr1))

print(arr1 + 5)



# ----aliasing----

aliasarr1 = np.array([2 , 6 , 8 ,3 ,6] ,int)

aliasarr2 = aliasarr1

print(aliasarr1 , aliasarr2)

print(id(aliasarr1))
print(id(aliasarr2))

# ---shallowcopy---

shalarr1 = np.array([2 , 6 , 8 ,3 ,6] ,int)
shalarr2 = shalarr1.view()

shalarr1[1] = 7

print(shalarr1 , shalarr2)

print(id(shalarr1))
print(id(shalarr2))


#---deepcopy---

deeparr1 = np.array([2 , 6 , 8 ,3 ,6] ,int)
deeparr2 = deeparr1.copy()

deeparr1[1] = 7

print(deeparr1 , deeparr2)

print(id(deeparr1))
print(id(deeparr2))

