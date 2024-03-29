import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.arange(0,np.pi,0.1)
y = 2*np.sin(2*x)

plt.plot(x,y)
