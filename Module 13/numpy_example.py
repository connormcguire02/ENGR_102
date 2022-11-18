import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
x, y = np.meshgrid(x,y)
z = x**2 + y**2

ax.plot_surface(x,y,z, linewidth=0, antialiased=False)

plt.show()
>>>>>>> 76367302328a35ec55c44782eacaef410ce3b673
