import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.rcParams['text.usetex'] = True
plt.ioff()

# PIC_2

fig = plt.figure()
plt.grid()
plt.xlabel(r'$\Delta P,\,$athm')
plt.ylabel(r'$\Delta T,\,$K')

pressure = [3.00, 2.60, 2.20, 1.80, 1.40, 1.00]
pressure_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

t = [3.47, 3.02, 2.56, 2.14, 1.71, 1.38]
t_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

coef = np.polyfit(pressure, t, 1)
poly1d_fn = np.poly1d(coef)  # to create a linear function with coefficients

plt.plot(pressure, poly1d_fn(pressure), color ='orange')
plt.errorbar(pressure, t, xerr = pressure_err, yerr = t_err, fmt ='.', color ='black')
plt.savefig('PIC_2.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(pressure, t, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

# PIC_3

fig = plt.figure()
plt.grid()
plt.xlabel(r'$\Delta P,\,$athm')
plt.ylabel(r'$\Delta T,\,$K')

pressure = [3.00, 2.60, 2.20, 1.80, 1.40, 1.00]
pressure_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

t = [2.76, 2.36, 1.97, 1.59, 1.23, 0.96]
t_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

coef = np.polyfit(pressure, t, 1)
poly1d_fn = np.poly1d(coef)  # to create a linear function with coefficients

plt.plot(pressure, poly1d_fn(pressure), color ='orange')
plt.errorbar(pressure, t, xerr = pressure_err, yerr = t_err, fmt ='.', color ='black')
plt.savefig('PIC_3.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(pressure, t, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

# PIC_4

fig = plt.figure()
plt.grid()
plt.xlabel(r'$\Delta P,\,$athm')
plt.ylabel(r'$\Delta T,\,$K')

pressure = [3.00, 2.60, 2.20, 1.80, 1.40, 1.00]
pressure_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

t = [2.10, 1.85, 1.57, 1.27, 0.95, 0.65]
t_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

coef = np.polyfit(pressure, t, 1)
poly1d_fn = np.poly1d(coef)  # to create a linear function with coefficients

plt.plot(pressure, poly1d_fn(pressure), color ='orange')
plt.errorbar(pressure, t, xerr = pressure_err, yerr = t_err, fmt ='.', color ='black')
plt.savefig('PIC_4.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(pressure, t, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

# PIC_5

fig = plt.figure()
plt.grid()
plt.xlabel(r'$1/T,\,$1/K')
plt.ylabel(r'$\mu_{j-th},\,$K/athm')

mu = [1.06, 0.91, 0.73]
mu_err = [0.03, 0.02, 0.01]

ot = [0.00344, 0.00325, 0.00300]
ot_err = [0.0, 0.0, 0.0]

coef = np.polyfit(ot, mu, 1)
poly1d_fn = np.poly1d(coef)  # to create a linear function with coefficients

plt.plot(ot, poly1d_fn(ot), color ='orange')
plt.errorbar(ot, mu, xerr = ot_err, yerr = mu_err, fmt ='.', color ='black')
plt.savefig('PIC_5.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(ot, mu, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))
