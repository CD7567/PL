import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.ioff()
plt.rcParams['text.usetex'] = True

# Calculations

r1 = [9.96, 9.97, 10.05, 10.13, 10.34, 10.46]
r1_err = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

q1 = [1.16, 4.35, 31.05, 55.43, 126.00, 168.50]
q1_err = [0.01, 0.01, 0.03, 0.06, 0.13, 0.17]

r2 = [10.28, 10.29, 10.37, 10.44, 10.65, 10.83]
r2_err = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

q2 = [1.19, 4.47, 31.79, 56.60, 127.80, 169.48]
q2_err = [0.01, 0.01, 0.03, 0.06, 0.13, 0.17]

r3 = [10.65, 10.65, 10.74, 10.81, 11.01, 11.13]
r3_err = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

q3 = [1.75, 4.62, 32.75, 58.20, 131.02, 174.37]
q3_err = [0.01, 0.01, 0.04, 0.06, 0.13, 0.18]

r4 = [11.00, 11.02, 11.10, 11.17, 11.38, 11.50]
r4_err = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

q4 = [1.27, 4.77, 33.68, 59.70, 133.79, 177.76]
q4_err = [0.01, 0.01, 0.03, 0.06, 0.12, 0.16]

r5 = [11.38, 11.39, 11.47, 11.54, 11.75, 11.88]
r5_err = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

q5 = [1.31, 4.92, 34.60, 61.21, 136.57, 188.11]
q5_err = [0.01, 0.01, 0.03, 0.05, 0.12, 0.16]

p1, V1 = np.polyfit(q1, r1, 1, cov=True)
p2, V2 = np.polyfit(q2, r2, 1, cov=True)
p3, V3 = np.polyfit(q3, r3, 1, cov=True)
p4, V4 = np.polyfit(q4, r4, 1, cov=True)
p5, V5 = np.polyfit(q5, r5, 1, cov=True)

print("slope: {} +/- {}".format(p1[0], np.sqrt(V1[0][0])))
print("intercept: {} +/- {}".format(p1[1], np.sqrt(V1[1][1])))
print("slope: {} +/- {}".format(p2[0], np.sqrt(V2[0][0])))
print("intercept: {} +/- {}".format(p2[1], np.sqrt(V2[1][1])))
print("slope: {} +/- {}".format(p3[0], np.sqrt(V3[0][0])))
print("intercept: {} +/- {}".format(p3[1], np.sqrt(V3[1][1])))
print("slope: {} +/- {}".format(p4[0], np.sqrt(V4[0][0])))
print("intercept: {} +/- {}".format(p4[1], np.sqrt(V4[1][1])))
print("slope: {} +/- {}".format(p5[0], np.sqrt(V5[0][0])))
print("intercept: {} +/- {}".format(p5[1], np.sqrt(V5[1][1])))

# PIC_3

fig = plt.figure()
plt.grid()
plt.xlabel(r'$t,\, ^\circ$C')
plt.ylabel(r'$R,\,$Ohm')

temperature = [21.4, 30.1, 40.0, 50.0, 60.0]
temperature_err = [0.1, 0.1, 0.1, 0.1, 0.1]

resistance = [9.958, 10.270, 10.644, 11.003, 11.377]
resistance_err = [0.005, 0.005, 0.005, 0.005, 0.005]

coef = np.polyfit(temperature, resistance, 1)
poly1d_fn = np.poly1d(coef)  # to create a linear function with coefficients

plt.plot(temperature, poly1d_fn(temperature), color ='orange')
plt.errorbar(temperature, resistance, xerr = temperature_err, yerr = resistance_err, fmt ='.', color ='black')
plt.savefig('PIC_3.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(temperature, resistance, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

# PIC_4

fig = plt.figure()
plt.grid()
plt.xlabel(r'$\ln T,\,$')
plt.ylabel(r'$\ln \kappa,\,$')

drdt = p[0]
drdt_err = np.sqrt(V[0][0])

ktemp = []
ktemp_err = temperature_err

for it in temperature:
    ktemp.append(it + 273)

drdq = [p1[0], p2[0], p3[0], p4[0], p5[0]]

kappa = [0.027, 0.028, 0.028, 0.031, 0.032]
kappa_err = [0.001, 0.002, 0.002, 0.001, 0.001]

lnktemp = []
lnktemp_err = []

lnkappa = []
lnkappa_err = []

for i in range(0, 5):
    lnktemp.append(np.log(ktemp[i]))
    lnktemp_err.append(ktemp_err[i]/ktemp[i])

for i in range(0, 5):
    lnkappa.append(np.log(kappa[i]))
    lnkappa_err.append(kappa_err[i]/kappa[i])

coef = np.polyfit(lnktemp, lnkappa, 1)
poly1d_fn = np.poly1d(coef)  # to create a linear function with coefficients

plt.plot(lnktemp, poly1d_fn(lnktemp), color ='orange')
plt.errorbar(lnktemp, lnkappa, xerr = lnktemp_err, yerr = lnkappa_err, fmt ='.', color ='black')
plt.savefig('PIC_4.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(lnktemp, lnkappa, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))
