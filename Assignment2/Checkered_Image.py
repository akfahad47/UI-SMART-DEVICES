import numpy as np
import matplotlib.pyplot as plt

# Create an 8x8 array of zeros (black squares)
check = np.zeros((8, 8))

# Fill alternate squares with 1 (white squares)
check[::2, 1::2] = 1
check[1::2, ::2] = 1

# Display the checkered pattern with custom color
plt.imshow(check, cmap='Blues', interpolation='nearest')
plt.show()
