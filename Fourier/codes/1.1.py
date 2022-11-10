# Plotting x(t)

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

A = 12
f = 50
T = np.linspace(-3/(2*f), 3/(2*f), 1000)

def x(t):
    return A * np.abs(np.sin(2 * np.pi * f * t))

plt.plot(T, x(T))
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Plot of $x(t)$')
plt.grid()
plt.savefig('../figs/1.1.png')
plt.show()
