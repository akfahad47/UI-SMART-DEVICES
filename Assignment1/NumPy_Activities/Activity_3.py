import timeit
import numpy as np

a = np.random.rand(1000)

# Timing a**2
time_square = timeit.timeit('a**2', globals=globals(), number=1000)
print(f"Time for a**2: {time_square} seconds")

# Timing a + 1
time_add = timeit.timeit('a + 1', globals=globals(), number=1000)
print(f"Time for a+1: {time_add} seconds")
