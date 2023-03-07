import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.ioff()
plt.rcParams['text.usetex'] = True

# PIC_3

fig = plt.figure()
plt.grid()
plt.xlabel(r'$\nu / \nu_0$')
plt.ylabel(r'$U / U_0$')

freq_raw_1 = [1.360, 1.408, 1.443, 1.468, 1.493, 1.516, 1.538, 1.551, 1.575, 1.616, 1.653, 1.682, 1.700, 1.717, 1.742, 1.766, 1.794, 1.841]
volt_raw_1 = [1.42, 1.78, 2.21, 2.63, 2.98, 3.40, 3.81, 4.00, 4.15, 3.92, 3.39, 3.00, 2.82, 2.57, 2.40, 2.19, 1.99, 1.82]

freq_raw_2 = [1.522, 1.530, 1.537, 1.540, 1.548, 1.555, 1.561, 1.567, 1.575, 1.581, 1.587, 1.593, 1.600, 1.608, 1.613, 1.618, 1.627, 1.634]
volt_raw_2 = [7.2, 8.4, 9.4, 10.2, 12.1, 13.9, 16.0, 18.1, 18.6, 17.9, 16.1, 14.0, 12.2, 9.8, 9.6, 8.8, 7.6, 6.8]

freq_1 = []
volt_1 = []

freq_2 = []
volt_2 = []

for it in freq_raw_1:
    freq_1.append(it / 1.575)

for it in volt_raw_1:
    volt_1.append(it / 4.15)

for it in freq_raw_2:
    freq_2.append(it / 1.575)

for it in volt_raw_2:
    volt_2.append(it / 18.6)

plt.plot(freq_1, volt_1, color = 'orange', marker = '+')
plt.plot(freq_2, volt_2, color = 'blue', marker = '+')
plt.axhline(y = 0.707, color = 'red')
plt.legend([r'$R_1 = 0\, \mathrm{Ohm}$', r'$R_2 = 100\, \mathrm{Ohm}$', r'$U / U_0 = 0.707$'])
#plt.errorbar(t, sigma, xerr = x_err, yerr = y_err, fmt ='.', color ='black')
plt.savefig('PIC_3.png', dpi = 1200)
plt.close(fig)
