from skimage import data
import matplotlib.pyplot as plt

# Load an example image from scikit-image
image = data.camera()

# Display image properties
print("Data Type:", image.dtype)
print("Shape:", image.shape)

# Plot the original image
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.show()

# Apply Gaussian filter with sigma=5
from skimage import filters
image_gaussian = filters.gaussian(image, sigma=5)

# Plot the image with Gaussian noise
plt.imshow(image_gaussian, cmap='gray')
plt.title('Image with Gaussian Filter (sigma=5)')
plt.show()
