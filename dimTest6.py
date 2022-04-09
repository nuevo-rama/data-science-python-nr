from operator import matmul
import numpy as np

# matmul Function
matrixOne = np.array([[1,2,3],[4,5,6],[0,0,0]])
print(matrixOne.ndim)

matrixTwo = np.array([[-1,-2,-3],[-4,-5,-6],[0,0,0]])
print(matrixTwo.ndim)

res = np.matmul(matrixOne, matrixTwo)
print(res)
