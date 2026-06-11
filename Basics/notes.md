[1,2,3,4,5,6,7,8,9] # vector

[
[1,2,3],  # matrix
[4,5,6]
]

## numpy array and basics
import numpy as np
arr_1d = np.array([1,2,3]) 
print("1D array",arr_1d)

arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D array",arr_2d)

## list vs numpy

py_list = [1,2,3]
print("python list mulitiplication",py_list *2)
arr = np.array([1,2,3])
print("python array mulitiplication",py_list *2) ## numpy is fast

## creating array from scratch

zeros = np.zeros([3,4])
print(" zeros array : \n",zeros)

onece = np.ones([3,3])
print("onece array : \n",onece)

full =np.full([2,2],7)
print("full array : \n",full)

random = np.random.random([2,3])
print("random array : \n",random)

sequence = np.arange(0,11,2)
print("sequence array : \n",sequence)

## vector , matrix , tensor

vector = np.array([1,2,3,4])
print("vector \n", vector)

array = np.array([[1,2,3],
                  [4,5,6]])
print("array \n", array)

tensor = np.array([[[1,3],[4,5],
                    [5,6],[8,9]]])

print("tensor \n", tensor)

## properties of array

print("shape" ,array.shape)
print("Dimentions" ,array.ndim)
print("size" ,array.size)
print("type" ,array.dtype)
