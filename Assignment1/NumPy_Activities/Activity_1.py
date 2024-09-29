import numpy as np

# Using arange
arr_arange = np.arange(10)
print("arange:", arr_arange, "Length:", len(arr_arange), "Shape:", arr_arange.shape)

# Using linspace
arr_linspace = np.linspace(0, 9, 10)
print("linspace:", arr_linspace, "Length:", len(arr_linspace), "Shape:", arr_linspace.shape)

# Using ones
arr_ones = np.ones((3, 3))
print("ones:\n", arr_ones, "Length:", len(arr_ones), "Shape:", arr_ones.shape)

# Using zeros
arr_zeros = np.zeros((2, 5))
print("zeros:\n", arr_zeros, "Length:", len(arr_zeros), "Shape:", arr_zeros.shape)

# Using eye
arr_eye = np.eye(4)
print("eye:\n", arr_eye, "Length:", len(arr_eye), "Shape:", arr_eye.shape)

# Using diag
arr_diag = np.diag([1, 2, 3, 4])
print("diag:\n", arr_diag, "Length:", len(arr_diag), "Shape:", arr_diag.shape)
