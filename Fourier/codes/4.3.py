# Convolution to get 5V DC output

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import subprocess
import shlex

A = 12
f = 50
V = 5
fc = 50

T = np.linspace(-1e5, 1e5, 100000)

def x(t):
    return A * np.abs(np.sin(2 * np.pi * f * t))

def h(t):
    return V * np.pi * 2 * fc / A * np.sinc(2 * fc * t)

X = x(T)
H = h(T)
Y = np.convolve(X, H)

plt.plot(Y)
plt.grid()
plt.xticks(color='w')
plt.title('Convolution to get 5V DC')
plt.savefig('../figs/4.3.png')
#plt.show()
#subprocess.run(shlex.split("termux-open ../figs/4.3.png"))
