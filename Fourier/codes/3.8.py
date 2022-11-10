# Plotting the Fourier transform of x(t)

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import subprocess
import shlex

A = 12
f = 50
N = 1000
t0 = 3/(2*f)
dt = 2*t0/N

T = np.linspace(-t0, t0, N)

def x(t):
    return A * np.abs(np.sin(2 * np.pi * f * t))

xt = x(T)
Xf = np.fft.fft(xt)
w = np.fft.fftfreq(len(xt)) * 2 * np.pi / dt
Xf *= dt * np.exp(1j * w * t0) / np.sqrt(2 * np.pi)

plt.plot(w, np.abs(Xf))
plt.gca().set_xlim(-1e4, 1e4)
plt.grid()
plt.title('Fourier Transform of $x(t)$')
plt.savefig('../figs/3.8.png')
#plt.show()
#subprocess.run(shlex.split("termux-open ../figs/3.8.png"))
