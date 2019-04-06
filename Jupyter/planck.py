#Graphing planck function
import matplotlib.pyplot as plt
import numpy as np
import math

lambda_min = 42
lambda_max = 5000

T = 5778
h, c, kB = 6.6206957e-34, 299792458, 1.3806488e-23

n = 50000
x = np.linspace(lambda_min, lambda_max, n)
y = 2*x
y = 2*h*(c**2)/(x**5)*(1)/(np.exp(h*c/x/kB/T) - 1)

line = plt.plot(x, y)
plt.xlabel("Lambda")
plt.ylabel("Spectral Radiance")
plt.xlim(lambda_max, 0)
plt.show()
