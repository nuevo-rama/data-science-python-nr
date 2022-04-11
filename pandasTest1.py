import pandas as pd
import numpy as np

# Data Frames from Lists

newList = [['a','b','c'],['d','e','f'],['g','h','i']]
newDataFrame = pd.DataFrame(newList)
print(newDataFrame)

newList = [['1982','01','01'],['1983','01','01'],['1984','01','01']]
newDataFrame = pd.DataFrame(newList, columns=["Year", "Month", "Day"])
print(newDataFrame)


# Data Frames from numPy arrays

newArrayNp = np.array([[1,2,3],[4,5,6],[0,0,0]])
newDataFrameNp = pd.DataFrame(newArrayNp)
print(newDataFrameNp)

# Data Frames using Dictionary

newDictionary = {"year":["1982", "1983", "1984"], "month":["01", "02", "03"]}
newDataFrameDn = pd.DataFrame(newDictionary)
print(newDataFrameDn)

# Loading CSV file as a Data Frame

dataFileCSV = pd.read_csv('dataFile.csv')
print(dataFileCSV)

# Head and Tail of the Data Frame

print(newDataFrameDn.head(1))

print(newDataFrameDn.tail(1))

# Statiscal Summary

print(newDataFrameDn.describe())

# Row Slicing

print(newDataFrameDn[0:2])
