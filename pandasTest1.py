import pandas as pd
import numpy as np

newList = [['a','b','c'],['d','e','f'],['g','h','i']]
newDataFrame = pd.DataFrame(newList)
print(newDataFrame)

newList = [['1982','01','01'],['1983','01','01'],['1984','01','01']]
newDataFrame = pd.DataFrame(newList, columns=["Year", "Month", "Day"])
print(newDataFrame)

newListNp = np.array([[1,2,3],[4,5,6],[0,0,0]])
newDataFrameNp = pd.DataFrame(newListNp)
print(newDataFrameNp)
