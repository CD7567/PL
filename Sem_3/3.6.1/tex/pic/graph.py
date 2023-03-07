import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.ioff()
plt.rcParams['text.usetex'] = True

# PIC_6

fig = plt.figure()
plt.grid()
plt.xlabel(r'$1/\tau,\, \mu s^{-1}$')
plt.ylabel(r'$\nu,\,kHz$')

t = [40, 60, 80, 100, 120, 140, 160, 180, 200]
inv_t = []

for it in t:
    inv_t.append(1/it)

nu = [25, 17, 13, 10, 8, 7, 6, 5.5, 5]
nu_err = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]


coef = np.polyfit(inv_t, nu, 1)
poly = np.poly1d(coef)

p, V = np.polyfit(inv_t, nu, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

lin_nu = poly(inv_t)

plt.plot(inv_t, lin_nu, color = 'orange')
plt.errorbar(inv_t, nu, yerr = nu_err, fmt ='.', color ='black')


plt.legend([r'Linear fit'])
plt.savefig('PIC_6.png', dpi = 1200)
plt.close(fig)

# PIC_12

fig = plt.figure()
plt.grid()
plt.xlabel(r'$1/T = \nu_0,\,kHz$')
plt.ylabel(r'$\delta\nu,\,kHz$')

nu0 = [0.5, 1, 2, 4, 5]
nu0_err = []

dnu = [0.5, 1, 2, 4, 5]
dnu_err = []

coef = np.polyfit(nu0, dnu, 1)
poly = np.poly1d(coef)
lin_nu = poly(nu0)

plt.plot(nu0, lin_nu, color = 'orange')
plt.errorbar(nu0, dnu, fmt ='.', color ='black')

plt.legend([r'Linear fit'])

plt.savefig('PIC_12.png', dpi = 1200)
plt.close(fig)

# PIC_13

fig = plt.figure()
plt.grid()
plt.xlabel(r'$A,\ V$')
plt.ylabel(r'$m$')

A = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
A_err = []

m = [0.104, 0.199, 0.307, 0.417, 0.495, 0.599, 0.705, 0.806, 0.893, 0.966]
m_err = []

coef = np.polyfit(A, m, 1)
poly = np.poly1d(coef)
lin_m = poly(A)

plt.plot(A, lin_m, color = 'orange')
plt.errorbar(A, m, fmt ='.', color ='black')

plt.legend([r'Linear fit'])

plt.savefig('PIC_13.png', dpi = 1200)
plt.close(fig)

# PIC_14

fig = plt.figure()
plt.grid()
plt.xlabel(r'$A_{side} / A_{main}$')
plt.ylabel(r'$m$')

fr = [0.048, 0.097, 0.149, 0.197, 0.246, 0.289, 0.341, 0.396, 0.440, 0.500]
fr_err = []

m = [0.104, 0.199, 0.307, 0.417, 0.495, 0.599, 0.705, 0.806, 0.893, 0.966]
m_err = []


coef = np.polyfit(fr, m, 1)
poly = np.poly1d(coef)

p, V = np.polyfit(fr, m, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

lin_m = poly(fr)

plt.plot(fr, lin_m, color = 'orange')
plt.errorbar(fr, m, fmt ='.', color ='black')


plt.legend([r'Linear fit'])
plt.savefig('PIC_14.png', dpi = 1200)
plt.close(fig)
