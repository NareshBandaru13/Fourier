# Plotting the Fourier transform of rect(t)

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import subprocess
import shlex

N = 10000
t0 = 100
dt = 2*t0/N

T = np.linspace(-t0, t0, N)
W = np.linspace(-100, 100, 200)

def rect_scalar(t):
    if np.abs(t) > 0.5:
        return 0
    else:
        return 1
    
rect = sp.vectorize(rect_scalar)

xt = rect(T)
Xf = np.fft.fft(xt)
w = np.fft.fftfreq(len(xt)) * 2 * np.pi / dt
Xf *= dt * np.exp(1j * w * t0) / np.sqrt(2 * np.pi)

plt.plot(w, np.abs(Xf), label='Simulation')
#plt.plot(W, np.sinc(W), label='Theoretical')
plt.gca().set_xlim(-1e2, 1e2)
plt.xticks(color='w')
plt.grid()
plt.title('Fourier Transform of $\mathrm{rect}(t)$')
#plt.legend()
plt.savefig('../figs/3.9.png')
#plt.show()
#subprocess.run(shlex.split("termux-open ../figs/3.8.png"))
