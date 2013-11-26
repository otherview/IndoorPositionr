import numpy as np
import matplotlib.pyplot as plt
x, y = np.meshgrid(np.arange(-10,10),np.arange(-10,10))
z = np.sqrt(x**2 + y**2)
cs = plt.contourf(x,y,z,levels=np.arange(-10.0,10.0,0.5))


plt.show()