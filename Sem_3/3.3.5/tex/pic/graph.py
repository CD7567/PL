import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.ioff()
plt.rcParams['text.usetex'] = True

# PIC_4

fig = plt.figure()
plt.grid()
plt.xlabel(r'$I,\, A$')
plt.ylabel(r'$B,\,T$')

I = [0, 0.20, 0.35, 0.50, 0.65, 0.80, 0.96]
I_err = [0, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

B = [0, 0.230, 0.400, 0.580, 0.780, 0.930, 1.050]
B_err = [0, 0.010, 0.020, 0.030, 0.040, 0.050, 0.055]


coef = np.polyfit(I, B, 1)
poly = np.poly1d(coef)

p, V = np.polyfit(I, B, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

lin_B = poly(I)

plt.plot(I, lin_B, color = 'orange')
plt.errorbar(I, B, xerr = I_err, yerr = B_err, fmt ='.', color ='black')

plt.legend([r'Linear fit'])
plt.savefig('PIC_4.png', dpi = 1200)
plt.close(fig)

# PIC_5

fig = plt.figure()
plt.grid()
plt.xlabel(r'$B,\,T$')
plt.ylabel(r'$U_\perp,\,nV$')

B_1 = [0.236, 0.450, 0.687, 0.912, 1.148, 1.362]
B_1_err = [0.026, 0.032, 0.039, 0.045, 0.052, 0.059]

B_2 = [0.236, 0.461, 0.687, 0.912, 1.137, 1.362]
B_2_err = [0.026, 0.032, 0.039, 0.045, 0.052, 0.059]

B_3 = [0.236, 0.461, 0.687, 0.912, 1.137, 1.362]
B_3_err = [0.026, 0.032, 0.039, 0.045, 0.052, 0.059]

B_4 = [0.236, 0.461, 0.687, 0.912, 1.137, 1.362]
B_4_err = [0.026, 0.032, 0.039, 0.045, 0.052, 0.059]


U_1 = [40, 120, 200, 280, 320, 360]
U_1_err = [40, 40, 40, 40, 40, 40]

U_2 = [80, 240, 400, 480, 560, 640]
U_2_err = [40, 40, 40, 40, 40, 40]

U_3 = [160, 280, 520, 640, 800, 920]
U_3_err = [40, 40, 40, 40, 40, 40]

U_4 = [160, 400, 640, 880, 1000, 1120]
U_4_err = [40, 40, 40, 40, 40, 40]


coef_1 = np.polyfit(B_1, U_1, 1)
poly_1 = np.poly1d(coef_1)
lin_1 = poly_1(B_1)

p_1, V_1 = np.polyfit(B_1, U_1, 1, cov=True)
print("slope: {} +/- {}".format(p_1[0], np.sqrt(V_1[0][0])))
print("intercept: {} +/- {}".format(p_1[1], np.sqrt(V_1[1][1])))
print("\n")

coef_2 = np.polyfit(B_2, U_2, 1)
poly_2 = np.poly1d(coef_2)
lin_2 = poly_2(B_2)

p_2, V_2 = np.polyfit(B_2, U_2, 1, cov=True)
print("slope: {} +/- {}".format(p_2[0], np.sqrt(V_2[0][0])))
print("intercept: {} +/- {}".format(p_2[1], np.sqrt(V_2[1][1])))
print("\n")

coef_3 = np.polyfit(B_3, U_3, 1)
poly_3 = np.poly1d(coef_3)
lin_3 = poly_3(B_3)

p_3, V_3 = np.polyfit(B_3, U_3, 1, cov=True)
print("slope: {} +/- {}".format(p_3[0], np.sqrt(V_3[0][0])))
print("intercept: {} +/- {}".format(p_3[1], np.sqrt(V_3[1][1])))
print("\n")

coef_4 = np.polyfit(B_4, U_4, 1)
poly_4 = np.poly1d(coef_4)
lin_4 = poly_4(B_4)

p_4, V_4 = np.polyfit(B_4, U_4, 1, cov=True)
print("slope: {} +/- {}".format(p_4[0], np.sqrt(V_4[0][0])))
print("intercept: {} +/- {}".format(p_4[1], np.sqrt(V_4[1][1])))

plt.plot(B_1, lin_1, color = 'red')
plt.errorbar(B_1, U_1, xerr = B_1_err, yerr = U_1_err, fmt = 'o', color = 'black')

plt.plot(B_2, lin_2, color = 'lime')
plt.errorbar(B_2, U_2, xerr = B_2_err, yerr = U_2_err, fmt = '^', color = 'black')

plt.plot(B_3, lin_3, color = 'blue')
plt.errorbar(B_3, U_3, xerr = B_3_err, yerr = U_3_err, fmt = 's', color = 'black')

plt.plot(B_4, lin_4, color = 'cyan')
plt.errorbar(B_4, U_4, xerr = B_4_err, yerr = U_4_err, fmt = 'D', color = 'black')

plt.legend([r'Linear fit, I = 0.4 A', r'Linear fit, I = 0.6 A', r'Linear fit, I = 0.8 A', r'Linear fit, I = 1.0 A'])

plt.savefig('PIC_5.png', dpi = 1200)
plt.close(fig)

# PIC_6

fig = plt.figure()
plt.grid()
plt.xlabel(r'$I,\,A$')
plt.ylabel(r'$k,\,V/T$')

I = [0.40, 0.60, 0.80, 1.00]
I_err = [0.01, 0.01, 0.01, 0.01]

k = [2.86, 4.87, 6.95, 8.68]
k_err = [0.22, 0.44, 0.35, 0.66]

k_fixed = []
k_fixed_err = []

for it in k:
    k_fixed.append(it / 10000000)
    
for it in k_err:
    k_fixed_err.append(it / 10000000)
    
coef = np.polyfit(I, k_fixed, 1)
poly = np.poly1d(coef)
lin = poly(I)

plt.plot(I, lin, color = 'orange')
plt.errorbar(I, k_fixed, xerr = I_err, yerr = k_fixed_err, fmt = '.', color = 'black')

p, V = np.polyfit(I, k_fixed, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))
print("\n")

plt.legend([r'Linear fit'])
plt.savefig('PIC_6.png', dpi = 1200)
plt.close(fig)

# PIC_7

fig = plt.figure()
plt.grid()
plt.xlabel(r'$B,\,T$')
plt.ylabel(r'$U_\perp,\,nV$')

B = [0.236, 0.461, 0.687, 0.912, 1.137, 1.362]
B_err = [0.026, 0.032, 0.039, 0.045, 0.052, 0.059]

U = [240, 480, 680, 800, 920, 1040]
U_err = [40, 40, 40, 40, 40, 40]
    
coef = np.polyfit(B, U, 1)
poly = np.poly1d(coef)
lin = poly(B)

plt.plot(B, lin, color = 'orange')
plt.errorbar(B, U, xerr = B_err, yerr = U_err, fmt = '.', color = 'black')

p, V = np.polyfit(B, U, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))
print("\n")

plt.legend([r'Linear fit'])
plt.savefig('PIC_7.png', dpi = 1200)
plt.close(fig)
