from cmath import sqrt
import math as math
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.ioff()
plt.rcParams['text.usetex'] = True

# PIC_8

fig = plt.figure()
plt.grid()
plt.xlabel(r'$|\cos\alpha|$')
plt.ylabel(r'$V_3\,\mathrm{units}$')

alpha_deg = [80, 75, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20]
alpha_deg_err = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

H_1 = [1.3, 1.3, 1.3, 1.25, 1.2, 1.15, 1.15, 1.15, 1.15, 1.15, 1.1, 1.1]
H_2 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.25, 0.3, 0.4, 0.6, 0.6, 0.8, 1]
H_3 = [1.4, 1.4, 1.2, 1, 0.9, 0.7, 0.6, 0.5, 0.4, 0.4, 0.4, 0.6]
H_4 = [1.4, 1.6, 1.6, 1.6, 1.8, 1.9, 2.2, 2.4, 2.85, 3, 3.2, 3.4]

H_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

alpha = [i * 2 * math.pi / 360 for i in alpha_deg]
alpha_err = [i * 2 * math.pi / 360 for i in alpha_deg_err]

delta = [h_1 / h_2 for h_1, h_2 in zip(H_1, H_2)]
delta_err = [sh / h_2 * math.sqrt(1 + (h_1 / h_2) ** 2) for h_1, h_2, sh in zip(H_1, H_2, H_err)]
inv_V_1 = [(1 + d) / 2 / math.sqrt(d) for d in delta]
inv_V_1_err = [abs(d - 1) / 4 / d / math.sqrt(d) * d_e for d, d_e in zip(delta, delta_err)]

V = [(h_4 - h_3) / (h_4 + h_3) * inv_1 for inv_1, h_3, h_4 in zip(inv_V_1, H_3, H_4)]
V_err = [math.sqrt((2 * inv_1 * sh/ (h_3 + h_4)) ** 2 * (h_3 ** 2 + h_4 ** 2) + ((h_4 - h_3) * sinv) ** 2) for h_3, h_4, inv_1, sh, sinv in zip(H_3, H_4, inv_V_1, H_err, inv_V_1_err)]

cos = [math.cos(a) for a in alpha]
cos_err = [max(abs(math.cos(a) - math.cos(a + a_err)), abs(math.cos(a) - math.cos(a - a_err))) for a, a_err in zip(alpha, alpha_err)]

#for a, sa, h_1, h_2, h_3, h_4, sh, v, sv in zip(alpha_deg, alpha_deg_err, H_1, H_2, H_3, H_4, H_err, V, V_err):
#    print(f'{a} $\pm$ {sa}', f'{"%.2f" % h_1} $\pm$ {sh}', f'{"%.2f" % h_2} $\pm$ {sh}', f'{"%.2f" % h_3} $\pm$ {sh}', f'{"%.2f" % h_4} $\pm$ {sh}', f'{"%.2f" % v} $\pm$ {"%.2f" % sv}', sep = ' & ', end = '\n \\\\\\hline\n')

coef = np.polyfit(cos, V, 1)
poly = np.poly1d(coef)

p, v = np.polyfit(cos, V, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(v[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(v[1][1])))

lin_V = poly(cos)

plt.plot(cos, lin_V, color = 'orange')
plt.errorbar(cos, V, xerr = cos_err, yerr = V_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_8.eps', format = 'eps')
plt.close(fig)

# PIC_9

fig = plt.figure()
plt.grid()
plt.xlabel(r'$x,\,\mathrm{cm}$')
plt.ylabel(r'$V_2\,\mathrm{units}$')

X = [10, 17, 24, 31, 38, 45, 52, 59, 66, 73, 75, 71, 8, 80, 12, 44, 33, 55]
X_err = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

H_1 = [0.65, 0.8, 1, 1.2, 1.2, 1.85, 1.8, 2.1, 2, 2.3, 1.6, 2.1, 1.1, 1.4, 1.1, 2.2, 1.7, 1.1]
H_2 = [1, 1, 1, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
H_3 = [0.6, 0.4, 1, 1.9, 1.3, 2.2, 2.4, 2.6, 2.6, 1.8, 1, 2.2, 1, 0.6, 0.6, 1.8, 2.4, 1.8]
H_4 = [2.4, 1.8, 2.4, 2.1, 1.6, 2.6, 3.2, 3.1, 2.8, 4.4, 3.6, 4.2, 2.7, 3.6, 3.2, 2.2, 2.6, 2.0]

H_err = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

tmp = sorted(zip(X, H_1, H_2, H_3, H_4), key = lambda x: x[0])

X = [x[0] for x in tmp]
H_1 = [x[1] for x in tmp]
H_2 = [x[2] for x in tmp]
H_3 = [x[3] for x in tmp]
H_4 = [x[4] for x in tmp]

delta = [h_1 / h_2 for h_1, h_2 in zip(H_1, H_2)]
delta_err = [sh / h_2 * math.sqrt(1 + (h_1 / h_2) ** 2) for h_1, h_2, sh in zip(H_1, H_2, H_err)]
inv_V_1 = [(1 + d) / 2 / math.sqrt(d) for d in delta]
inv_V_1_err = [abs(d - 1) / 4 / d / math.sqrt(d) * d_e for d, d_e in zip(delta, delta_err)]

V = [(h_4 - h_3) / (h_4 + h_3) * inv_1 for inv_1, h_3, h_4 in zip(inv_V_1, H_3, H_4)]
V_err = [math.sqrt((2 * inv_1 * sh/ (h_3 + h_4)) ** 2 * (h_3 ** 2 + h_4 ** 2) + ((h_4 - h_3) * sinv) ** 2) for h_3, h_4, inv_1, sh, sinv in zip(H_3, H_4, inv_V_1, H_err, inv_V_1_err)]

#for x, sx, h_1, h_2, h_3, h_4, sh, v, sv in zip(X, X_err, H_1, H_2, H_3, H_4, H_err, V, V_err):
#    print(f'{x} $\pm$ {sx}', f'{"%.2f" % h_1} $\pm$ {sh}', f'{"%.2f" % h_2} $\pm$ {sh}', f'{"%.2f" % h_3} $\pm$ {sh}', f'{"%.2f" % h_4} $\pm$ {sh}', f'{"%.2f" % v} $\pm$ {"%.2f" % sv}', sep = ' & ', end = '\n \\\\\\hline\n')

plt.axvline(x = 15, color = 'orange', label = 'First maximum')
plt.axvline(x = 80, color = 'orange', label = 'Second maximum')
plt.errorbar(X, V, xerr = X_err, yerr = V_err, fmt ='.', color ='black')

plt.savefig('PIC_9.eps', format = 'eps')
plt.savefig('PIC_9.png')
plt.close(fig)
