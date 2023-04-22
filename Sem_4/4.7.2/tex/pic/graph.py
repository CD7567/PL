from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.ioff()
plt.rcParams['text.usetex'] = True

# PIC_5

fig = plt.figure()
plt.grid()
plt.xlabel(r'$m$')
plt.ylabel(r'$r_m^2,\, \mathrm{cm}$')

m = [1, 2, 3, 4, 5]

r = [2.8, 4.0, 5.0, 5.7, 6.5]
r_err = [0.5, 0.5, 0.5, 0.5, 0.5]

r_sqr = [i**2 for i in r]
r_sqr_err = [i**2 for i in r_err]

coef = np.polyfit(m, r_sqr, 1)
poly = np.poly1d(coef)

p, V = np.polyfit(m, r_sqr, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

lin_r_sqr = poly(m)

plt.plot(m, lin_r_sqr, color = 'orange')
plt.errorbar(m, r_sqr, yerr = r_sqr_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_5.eps', format = 'eps')
plt.close(fig)
