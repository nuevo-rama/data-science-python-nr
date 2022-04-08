import numpy as np


d1 = np.array([1,2,3,4,5])
print(d1)
print("index: ", d1[2])
print("ndim: ", d1.ndim)
print("shape: ", d1.shape)


d2 = np.array([[1,2,3,4,5],[-1,-2,-3,-4,-5]])
print(d2)
print("ndim: ", d2.ndim)
print("index: ", d2[1])
print("index: ", d2[0,2])
print("index: ", d2[1,2])
print("shape: ", d2.shape)



d3 = np.array([[[1,2,3,4,5],[-1,-2,-3,-4,-5]],[[6,7,8,9,10],[-6,-7,-8,-9,-10]]])
print(d3)
print("ndim: ", d3.ndim)
print("index: ", d3[0])
print("index: ", d3[0,1])
print("index: ", d3[0,1,2])
print("shape: ", d3.shape)
