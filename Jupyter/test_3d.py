import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("periodicity/stm.txt", float)


from mpl_toolkits.mplot3d import Axes3D


plt.imshow(data)

fig = plt.figure()
shape = data.shape
print(shape)
xs = np.arange(shape[0])
ys = np.arange(shape[1])
mesh = np.meshgrid(ys, xs)
print(mesh[0].shape)
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(mesh[1], mesh[0], data)

c = np.fft.fft(data)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

mesh = np.meshgrid(ys[9:-1], xs)
print(c[:,9:-1].shape)
print(mesh[0].shape)
ax1.plot_wireframe(mesh[1], mesh[0], abs(c[:,9:-1])**2)

plt.show()
