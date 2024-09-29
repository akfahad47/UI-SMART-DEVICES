import matplotlib.pyplot as plt

# Solid line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b-')
plt.title('Solid Line')
plt.savefig('Fig1.png')  
plt.show() 
plt.clf()   

# Dotted line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r:')
plt.title('Dotted Line')
plt.savefig('Fig2.png')
plt.show()
plt.clf()

# Dashed line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g--')
plt.title('Dashed Line')
plt.savefig('Fig3.png')
plt.show()
plt.clf()
