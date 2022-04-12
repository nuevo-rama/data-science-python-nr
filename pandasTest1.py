import pandas as pd
import numpy as np

# Data Frames from Lists

newList = [['a','b','c'],['d','e','f'],['g','h','i']]
newDataFrame = pd.DataFrame(newList)
print('Data Frame from Lists: \n' , newDataFrame)

newList = [[1982,1,1],[1983,1,1],[1984,1,1]]
newDataFrame = pd.DataFrame(newList, columns=["Year", "Month", "Day"])
print('Data Frame from Lists: \n' , newDataFrame)

#-------------------------------------------------

# Data Frames from numPy arrays

newArrayNp = np.array([[1,2,3],[4,5,6],[0,0,0]])
newDataFrameNp = pd.DataFrame(newArrayNp)
print('Data Frames from numPy arrays: \n' , newDataFrameNp)

#-------------------------------------------------

# Data Frames using Dictionary

newDictionary = {"year":[1982, 1983, 1984, 1985, 1986], "month":[1, 2, 3, 4, 5]}
newDataFrameDn = pd.DataFrame(newDictionary)
print('Data Frames using Dictionary: \n' , newDataFrameDn)

#-------------------------------------------------

# Loading CSV file as a Data Frame

#dataFileCSV = pd.read_csv('dataFile.csv')
#print(dataFileCSV)

#-------------------------------------------------

# Head and Tail of the Data Frame

print('Head of the Data Frame (1): \n' , newDataFrameDn.head(1))

print('Tail of the Data Frame (1): \n' , newDataFrameDn.tail(1))

#-------------------------------------------------

# Statiscal Summary

print('Statiscal Summary: \n' , newDataFrameDn.describe())

#-------------------------------------------------

# Row Slicing

print('Row Slicing: \n' , newDataFrameDn[0:2])

#-------------------------------------------------

# Indexing Columns with []

print('Indexing Columns with []: \n' , newDataFrameDn[['year']])

#-------------------------------------------------

# Boolean List

secondRow = [False, True, False, False, False]
print('Boolean List: \n' , newDataFrameDn[secondRow])

#-------------------------------------------------

# Filtering Rows

filterDataFrame = newDataFrameDn['year']>1982
print('Filtering Rows: \n' , newDataFrameDn[filterDataFrame])

#-------------------------------------------------

# Filtering Rows using & and |

filterDataFrame = newDataFrameDn[(newDataFrameDn['year'] > 1982) & (newDataFrameDn['month'] > 3)]
print('Filtering Rows using &: \n' , filterDataFrame)

filterDataFrame = newDataFrameDn[(newDataFrameDn['year'] > 1982) | (newDataFrameDn['month'] > 3)]
print('Filtering Rows using |: \n', filterDataFrame)

#-------------------------------------------------

# Filter using loc()

print('Filter using loc(): \n' , newDataFrameDn.loc[0, 'year'])

print('Filter using loc(): \n' , newDataFrameDn.loc[[0], ['year']])

print('Filter using loc(): \n' , newDataFrameDn.loc[0:3, 'year':'month'])

print('Filter using loc(): \n' , newDataFrameDn.loc[[0,4], 'year':'month'])

#-------------------------------------------------

# Filter using iloc()

print('Filter using iloc(): \n' , newDataFrameDn.iloc[0,1]) #[row,column]

print('Filter using iloc(): \n' , newDataFrameDn.iloc[0:2,0:1])

print('Filter using iloc(): \n' , newDataFrameDn.iloc[[0,2,3],0:1])

#-------------------------------------------------

# Add and Delete Rows and Columns

newDataFrameDn.loc[5] = [1990, 6]
print('Add Row: \n' , newDataFrameDn)

newDataFrameDn.drop(5, axis=0, inplace=True)
print('Delete Row: \n' , newDataFrameDn)

newDataFrameDn['Day'] = [1,2,3,4,5]
print('Add Column: \n' , newDataFrameDn)

newDataFrameDn.drop('Day', axis=1, inplace=True)
print('Delete Column: \n' , newDataFrameDn)

#-------------------------------------------------

# Sort Values

print(newDataFrameDn.sort_values(by='month', ascending=False))

#-------------------------------------------------

# Export and Save Pandas DataFrame

newDataFrameDn.to_csv('dataFrameTest.csv', index_label=False)

dataFrameTest = pd.read_csv('dataFrameTest.csv')
print(dataFrameTest)

#-------------------------------------------------

# Concatenate Dataframes

newDictionary1 = {"year":[1982, 1983, 1984, 1985, 1986], "month":[1, 2, 3, 4, 5]}
dataFrame1 = pd.DataFrame(newDictionary1)

newDictionary2 = {"year":[1987, 1988, 1989, 1990, 1991], "month":[1, 2, 3, 4, 5]}
dataFrame2 = pd.DataFrame(newDictionary2)

dataFrameConcat = pd.concat([dataFrame1, dataFrame2], axis=0)

print('DataFrames concatenate: \n' , dataFrameConcat)

#-------------------------------------------------

# groupby()

print(dataFrame1.groupby(dataFrame1['month']).mean())








