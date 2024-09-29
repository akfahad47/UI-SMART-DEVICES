

import numpy as np

# Creating a multidimensional array
arr_multi = np.arange(16).reshape(4, 4)
print("Original Array:\n", arr_multi)

# Reshaping
arr_reshaped = arr_multi.reshape(2, 8)
print("Reshaped Array:\n", arr_reshaped)

# Transposition
arr_transposed = arr_multi.T
print("Transposed Array:\n", arr_transposed)

# Statistics
print("Standard Deviation:", np.std(arr_multi))
print("Mean:", np.mean(arr_multi))
print("Median:", np.median(arr_multi))
