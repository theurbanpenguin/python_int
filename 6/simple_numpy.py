import numpy as np


# Example dataset with NaN values and an outlier
data = np.array([10, 12, np.nan, 15, 14, np.nan, 19, 120, 13, 18, 16])

print("Original data:")
print(data)

print("Original data with Not a Number removed:")
data_clean = data[~np.isnan(data)]
print(data_clean)

print("Original data with Not a Number changed to 0:")
data[np.isnan(data)] = 0
print(data)

print("Max value in data clean:")
maximum = np.max(data_clean)
print(maximum)

print("Min value in data clean:")
minimum = np.min(data_clean)
print(minimum)

print("Mean Average value in data clean:")
avg = np.mean(data_clean)
print(avg)

print("Median Average value in data clean:")
'''
Arrange all numbers in order 
If odd number print middle number
If even number print average of 2 middle numbers
'''
median = np.median(data_clean)
print(median)

