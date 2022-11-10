# Comparing x(t) with its Fourier series and complex Fourier series

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

A = 12
f = 50
T1 = np.linspace(-3/(2*f), 3/(2*f), 1000)
T2 = np.linspace(-3/(2*f), 3/(2*f), 100)

def x(t):
    return A * np.abs(np.sin(2 * np.pi * f * t))

def c(k):
    if k % 2:
        return 0
    else:
        return 2 * A / (np.pi * (1 - k**2))

c_vec = sp.vectorize(c)

def cexp(k, t):
    return np.exp(2j * np.pi * k * f * t)

def a(k):
    if k < 0:
        return 0
    elif k == 0:
        return 2 * A / np.pi
    elif k % 2 == 0:
        return 4 * A / (np.pi * (1 - k**2))
    else:
        return 0

a_vec = sp.vectorize(a)

def fcos(k, t):
    return np.cos(2 * np.pi * k * f * t)

def xFc(t):
    K = np.arange(-100, 101)
    E = cexp(K, t)
    C = c_vec(K)
    return np.sum(C * E)

xFc_vec = sp.vectorize(xFc)

def xF(t):
    K = np.arange(0, 101)
    Cos = fcos(K, t)
    A = a_vec(K)
    return np.sum(A * Cos)

xF_vec = sp.vectorize(xF)

plt.plot(T1, x(T1), label='Original')
plt.plot(T2, np.real(xF_vec(T2)), 'o', label='Fourier')
plt.plot(T2, np.real(xFc_vec(T2)), '.', label='Complex Fourier')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.title('Comparison of the Fourier series of $x(t)$')
plt.grid()
plt.legend()
plt.savefig('../figs/comparison.png')
plt.show()
