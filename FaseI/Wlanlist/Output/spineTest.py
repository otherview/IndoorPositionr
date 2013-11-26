import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os


import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(121)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

ax = plt.subplot(122)
plt.tight_layout()
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

img=mpimg.imread(os.path.dirname(__file__) + '\\..\\_Tratamento de Dados\\piso0-tagus.png')
imgplot1 = ax.imshow(img)
ax.autoscale_view('tight')


plt.subplots_adjust(hspace = .001)
plt.show()
