import numpy as np
import matplotlib.pyplot as plt

# Creating a random image
random_image = np.random.rand(10, 10)

# Hot color map
plt.imshow(random_image, cmap='hot')
plt.title('Random Image - Hot')
plt.savefig('Fig1_img.png')  
plt.show()  
plt.clf()   

# Cool color map
plt.imshow(random_image, cmap='cool')
plt.title('Random Image - Cool')
plt.savefig('Fig2_img.png') 
plt.show()  
plt.clf()   
