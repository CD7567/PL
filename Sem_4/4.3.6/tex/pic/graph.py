from cmath import sqrt
import math as math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

plt.ioff()
plt.rcParams['text.usetex'] = True

# Calculations

lamb = 0.000532
L = 1363
L_err = 5
x = [31, 24, 12, 6.5, 4.5]
x_err = [0.5, 0.5, 0.5, 0.5, 0.5]

d_1 = [lamb * L / i for i in x]
d_1_err = []

for dv, de in zip(x, x_err):
    d_1_err.append(sqrt((lamb * L_err / dv) ** 2 + (lamb * L * de / (dv ** 2)) ** 2).real)

output = [f'{"%.3f" % dv} $\pm$ {"%.3f" % de}' for dv, de in zip(d_1, d_1_err)]

print('\\hline\n$i$, \# & ', end = '')
print(*range(1, 6), sep = ' & ')
print('\\\\\\hline\n$d$, мм & ', end = '')
print(*output, sep = ' & ')
print('\\\\\\hline\n')

a = 5.5
b = 127.6
a_err = 0.5
b_err = 0.5

D = [0.5, 1, 1.5, 3, 4]
D_err = [0.1, 0.1, 0.1, 0.1, 0.1]
d_2 = [it * a / b for it in D]
d_2_err = []

for dv, de in zip(D, D_err):
    d_2_err.append(sqrt((a * de / b) ** 2 + (a_err * dv / b) ** 2 + (b_err * dv * a / (b ** 2)) ** 2).real)

output = [f'{"%.3f" % dv} $\pm$ {"%.3f" % de}' for dv, de in zip(d_2, d_2_err)]

print('\\hline\n$i$, \# & ', end = '')
print(*range(1, 6), sep = ' & ')
print('\\\\\\hline\n$d$, мм & ', end = '')
print(*output, sep = ' & ')
print('\\\\\\hline\n')

# PIC_6

fig = plt.figure()
plt.grid()
plt.xlabel(r'$n, \#$')
plt.ylabel(r'$z_{1,n}, \mathrm{cm}$')

num_1 = [0, 1, 2, 3, 4, 5, 6]

z_1 = [0.180, 0.250, 0.315, 0.380, 0.430, 0.475, 0.510]
z_1_err = [0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005]

coef = np.polyfit(num_1, z_1, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(num_1, z_1, 1, cov=True)
# print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
# print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

gamma_1 = [p[0], np.sqrt(v[0][0])]

lin_z_1 = poly(num_1)

plt.plot(num_1, lin_z_1, color = 'orange')
plt.errorbar(num_1, z_1, yerr = z_1_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_6.eps', format = 'eps')
plt.close(fig)

# PIC_7

fig = plt.figure()
plt.grid()
plt.xlabel(r'$n, \#$')
plt.ylabel(r'$z_{2,n}, \mathrm{cm}$')

num_2 = [0, 1, 2, 3, 4]

z_2 = [0.140, 0.410, 0.585, 0.750, 0.925]
z_2_err = [0.005, 0.005, 0.005, 0.005, 0.005]

coef = np.polyfit(num_2, z_2, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(num_2, z_2, 1, cov=True)
# print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
# print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

gamma_2 = [p[0], np.sqrt(v[0][0])]

lin_z_2 = poly(num_2)

plt.plot(num_2, lin_z_2, color = 'orange')
plt.errorbar(num_2, z_2, yerr = z_2_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_7.eps', format = 'eps')
plt.close(fig)

# PIC_8

fig = plt.figure()
plt.grid()
plt.xlabel(r'$n, \#$')
plt.ylabel(r'$z_{3,n}, \mathrm{cm}$')

num_3 = [0, 1, 2, 3, 4, 5]

z_3 = [0.180, 0.640, 0.940, 1.240, 1.640, 2.020]
z_3_err = [0.005, 0.005, 0.005, 0.005, 0.005, 0.005]

coef = np.polyfit(num_3, z_3, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(num_3, z_3, 1, cov=True)
# print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
# print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

gamma_3 = [p[0], np.sqrt(v[0][0])]

lin_z_3 = poly(num_3)

plt.plot(num_3, lin_z_3, color = 'orange')
plt.errorbar(num_3, z_3, yerr = z_3_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_8.eps', format = 'eps')
plt.close(fig)

# PIC_9

fig = plt.figure()
plt.grid()
plt.xlabel(r'$n, \#$')
plt.ylabel(r'$z_{4,n}, \mathrm{cm}$')

num_4 = [0, 1, 2, 3, 4]

z_4 = [0.180, 1.245, 2.770, 3.850, 5.470]
z_4_err = [0.005, 0.005, 0.005, 0.005, 0.005]

coef = np.polyfit(num_4, z_4, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(num_4, z_4, 1, cov=True)
# print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
# print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

gamma_4 = [p[0], np.sqrt(v[0][0])]

lin_z_4 = poly(num_4)

plt.plot(num_4, lin_z_4, color = 'orange')
plt.errorbar(num_4, z_4, yerr = z_4_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_9.eps', format = 'eps')
plt.close(fig)

# PIC_10

fig = plt.figure()
plt.grid()
plt.xlabel(r'$n, \#$')
plt.ylabel(r'$z_{5,n}, \mathrm{cm}$')

num_5 = [0, 1, 2]

z_5 = [0.180, 2.105, 5.140]
z_5_err = [0.005, 0.005, 0.005]

coef = np.polyfit(num_5, z_5, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(num_5, z_5, 1, cov=True)
# print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
# print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

gamma_5 = [p[0], np.sqrt(v[0][0])]

lin_z_5 = poly(num_5)

plt.plot(num_5, lin_z_5, color = 'orange')
plt.errorbar(num_5, z_5, yerr = z_5_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_10.eps', format = 'eps')
plt.close(fig)

# Gamma Table

Gamma = [gamma_1, gamma_2, gamma_3, gamma_4, gamma_5]
gamma_table = [f'{"%.3f" % gamma[0]} $\pm$ {"%.3f" % gamma[1]}' for gamma in Gamma]

d = [sqrt(Gamma[i][0] * 10 * lamb / 0.5).real for i in range(5)]
d_err = [sqrt(Gamma[i][1] * 10 * lamb / (2 * Gamma[i][0])).real for i in range(5)]
d_table = [f'{"%.3f" % d[i]} $\pm$ {"%.3f" % d_err[i]}' for i in range(5)]

print('\\hline\n$i$, \# & ', end = '')
print(*range(1, 6), sep = ' & ')
print('\\\\\\hline\n$\gamma$, cм & ', end = '')
print(*gamma_table, sep = ' & ')
print('\\\\\\hline\n$d$, мм & ', end = '')
print(*d_table, sep = ' & ')
print('\\\\\\hline\n')

# PIC_11

fig = plt.figure()
plt.grid()
plt.xlabel(r'$n, \#$')
plt.ylabel(r'$z_{20,n}, \mathrm{cm}$')

num_20 = [0, 1, 2, 3, 4]

z_20 = [2.730, 3.040, 3.175, 3.324, 3.610]
z_20_err = [0.005, 0.005, 0.005, 0.005, 0.005]

coef = np.polyfit(num_20, z_20, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(num_20, z_20, 1, cov=True)
# print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
# print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

gamma_20 = [p[0], np.sqrt(v[0][0])]

lin_z_20 = poly(num_20)

plt.plot(num_20, lin_z_20, color = 'orange')
plt.errorbar(num_20, z_20, yerr = z_20_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_11.eps', format = 'eps')
plt.close(fig)

# PIC_12

fig = plt.figure()
plt.grid()
plt.xlabel(r'$n, \#$')
plt.ylabel(r'$z_{25,n}, \mathrm{cm}$')

num_25 = [0, 1, 2, 3, 4]

z_25 = [3.350, 3.525, 3.805, 4.275, 4.455]
z_25_err = [0.005, 0.005, 0.005, 0.005, 0.005]

coef = np.polyfit(num_25, z_25, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(num_25, z_25, 1, cov=True)
# print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
# print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

gamma_25 = [p[0], np.sqrt(v[0][0])]

lin_z_25 = poly(num_25)

plt.plot(num_25, lin_z_25, color = 'orange')
plt.errorbar(num_25, z_25, yerr = z_25_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_12.eps', format = 'eps')
plt.close(fig)

Gamma = [gamma_20, gamma_25]
gamma_table = [f'{"%.3f" % gamma[0]} $\pm$ {"%.3f" % gamma[1]}' for gamma in Gamma]

d = [sqrt(Gamma[i][0] * 10 * lamb / 2).real for i in range(2)]
d_err = [sqrt(Gamma[i][1] * 10 * lamb / (8 * Gamma[i][0])).real for i in range(2)]
d_table = [f'{"%.3f" % d[i]} $\pm$ {"%.3f" % d_err[i]}' for i in range(2)]

print('\\hline\n$i$, \# & ', end = '')
print(20, 25, sep = ' & ')
print('\\\\\\hline\n$\gamma$, cм & ', end = '')
print(*gamma_table, sep = ' & ')
print('\\\\\\hline\n$d$, мм & ', end = '')
print(*d_table, sep = ' & ')
print('\\\\\\hline\n')