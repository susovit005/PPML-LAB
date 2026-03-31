# Experiment - 11 : NumPy Arrays & Pandas
# ============================================================

import numpy as np
import pandas as pd


# Q1. WAP for ndarray Object, Indexing and Slicing

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Element at (0,1):", arr[0, 1])
print("Row:", arr[1:])
print("Column 2:", arr[:, 2])

# Output:
# Array:
#  [[1 2 3]
#   [4 5 6]]
# Element at (0,1): 20
# Row: [[40 50 60]]
# Column 2: [30 60]


# -------------------------------------------------------

# Q2. WAP for Data Types and Structures in Numpy

arr  = np.array([1, 2, 3], dtype='int32')
print("Data type:", arr.dtype)
arr2 = arr.astype('float64')
print("Updated type:", arr2.dtype)

# Output:
# Data type: int32
# Updated type: float64


# -------------------------------------------------------

# Q3. WAP for Numpy Array Properties and Functions

ones_array  = np.ones((2, 3))
zeros_array = np.zeros((2, 3))
empty_array = np.empty((2, 3))
print("Ones:\n", ones_array)
print("Zero:\n", zeros_array)
print("Empty:\n", empty_array)
arr      = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape of array:", arr.shape)
reshaped = arr.reshape(3, 2)
print("Reshaped array:\n", reshaped)

arr1       = np.array([0, 2, 3])
copy_arr1  = arr1.copy()
view_arr1  = arr1.view()
print("Original", arr1)
print("View:", view_arr1)

arr2         = np.array([1, 2])
arr3         = np.array([3, 4])
concatenated = np.concatenate((arr2, arr3))
print("Concatenated array:", concatenated)

arr4 = np.array([5, 2, 8, 1])
print("Sorted array:", np.sort(arr4))

# Output:
# Ones:
#  [[1. 1. 1.]
#   [1. 1. 1.]]
# Zero:
#  [[0. 0. 0.]
#   [0. 0. 0.]]
# Shape of array: (2, 3)
# Reshaped array:
#  [[1 2]
#   [3 4]
#   [5 6]]
# Original [0 2 3]
# View: [0 2 3]
# Concatenated array: [1 2 3 4]
# Sorted array: [1 2 5 8]


# -------------------------------------------------------

# Q4. WAP for Statistical Operation and Broadcasting on Arrays

arr = np.array([1, 2, 3, 4])
print("Max:", arr.max())
print("Min:", arr.min())
print("Sum:", arr.sum())
print("Product:", arr.prod())
print("Broadcast result:", arr + 5)

# Output:
# Max: 4
# Min: 1
# Sum: 10
# Product: 24
# Broadcast result: [ 6  7  8  9]


# -------------------------------------------------------

# Q5. WAP for Saving and Loading Arrays

arr        = np.array([1, 2, 3, 4])
np.save('my_array', arr)
loaded_arr = np.load('my_array.npy')
print("Loaded array:", loaded_arr)

# Output:
# Loaded array: [1 2 3 4]


# -------------------------------------------------------

# Q6. WAP to create and work with Pandas Series

data   = [10, 20, 30]
labels = ['a', 'b', 'c']
series = pd.Series(data, index=labels)
print("Pandas Series:")
print(series)
print("Value at label 'b':", series['b'])

# Output:
# Pandas Series:
# a    10
# b    20
# c    30
# dtype: int64
# Value at label 'b': 20


# -------------------------------------------------------

# Q7. WAP to create and manipulate a data frame

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age':  [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("Age Column:")
print(df['Age'])
# Access a row
print("Row at index1:")
print(df.iloc[1])

# Output:
# DataFrame:
#       Name  Age           City
# 0    Alice   25       New York
# 1      Bob   30  San Francisco
# 2  Charlie   35    Los Angeles
# Age Column:
# 0    25
# 1    30
# 2    35
# Name: Age, dtype: int64
# Row at index1:
# Name      Bob
# Age        30
# City  San Francisco


# -------------------------------------------------------

# Q8. WAP to read CSV and JSON files

df_csv  = pd.read_csv('sample.csv')
print("DataFrame from CSV:")
print(df_csv)

df_json = pd.read_json('sample.json')
print("DataFrame from JSON:")
print(df_json)

# Output:
# (Depends on file contents — table printed from sample.csv and sample.json)


# -------------------------------------------------------

# Q9. WAP to calculate the correlation between columns in data frame

data        = {'Math':    [90, 85, 80, 95],
               'Science': [88, 82, 85, 90],
               'English': [78, 75, 80, 85]}
df          = pd.DataFrame(data)
print("DataFrame:")
print(df)
correlation = df.corr()
print("Correlation Matrix:")
print(correlation)

# Output:
# DataFrame:
#    Math  Science  English
# 0    90       88       78
# 1    85       82       75
# 2    80       85       80
# 3    95       90       85
# Correlation Matrix:
#               Math   Science   English
# Math      1.000000  0.981981  0.981981
# Science   0.981981  1.000000  0.944911
# English   0.981981  0.944911  1.000000
