import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
from scipy.stats import linregress

plt.rcParams['text.usetex'] = True
plt.ioff()

# PIC_2

fig = plt.figure()
plt.grid()
plt.xlabel(r'$i,\,$num')
plt.ylabel(r'$l,\,$mm')

i_1 = [0, 1, 2, 3]
i_2 = [0, 1, 2, 3, 4]
i_3 = [0, 1, 2, 3, 4, 5]

l1 = [0, 63, 127, 192]
l1_err = [1, 1, 1, 1]

l2 = [0, 58, 115, 173]
l2_err = [1, 1, 1, 1]

l3 = [0, 50, 99, 149, 199]
l3_err = [1, 1, 1, 1, 1]

l4 = [0, 43, 86, 128, 171]
l4_err = [1, 1, 1, 1, 1]

l5 = [0, 38, 76, 115, 153, 192]
l5_err = [1, 1, 1, 1, 1, 1]


coef1 = np.polyfit(i_1, l1, 1)
poly1d_fn1 = np.poly1d(coef1)  # to create a linear function with coefficients

coef2 = np.polyfit(i_1, l2, 1)
poly1d_fn2 = np.poly1d(coef2)  # to create a linear function with coefficients

coef3 = np.polyfit(i_2, l3, 1)
poly1d_fn3 = np.poly1d(coef3)  # to create a linear function with coefficients

coef4 = np.polyfit(i_2, l4, 1)
poly1d_fn4 = np.poly1d(coef4)  # to create a linear function with coefficients

coef5 = np.polyfit(i_3, l5, 1)
poly1d_fn5 = np.poly1d(coef5)  # to create a linear function with coefficients

plt.plot(i_1, poly1d_fn1(i_1), color ='red')
plt.errorbar(i_1, l1, yerr = l1_err, fmt ='.', color ='black')

plt.plot(i_1, poly1d_fn2(i_1), color ='lime')
plt.errorbar(i_1, l2, yerr = l2_err, fmt ='.', color ='black')

plt.plot(i_2, poly1d_fn3(i_2), color ='blue')
plt.errorbar(i_2, l3, yerr = l3_err, fmt ='.', color ='black')

plt.plot(i_2, poly1d_fn4(i_2), color ='cyan')
plt.errorbar(i_2, l4, yerr = l4_err, fmt ='.', color ='black')

plt.plot(i_3, poly1d_fn5(i_3), color ='magenta')
plt.errorbar(i_3, l5, yerr = l5_err, fmt ='.', color ='black')

plt.legend(['2700 Hz', '2998 Hz', '3502 Hz', '4042 Hz', '4476 Hz'])

plt.savefig('PIC_2.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(i_1, l1, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_1, l2, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_2, l3, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_2, l4, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_3, l5, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

# PIC_3

fig = plt.figure()
plt.grid()
plt.xlabel(r'$i,\,$num')
plt.ylabel(r'$l,\,$mm')

i_1 = [0, 1, 2, 3]
i_2 = [0, 1, 2, 3, 4]

l1 = [0, 62, 122, 183]
l1_err = [1, 1, 1, 1]

l2 = [0, 55, 111, 167]
l2_err = [1, 1, 1, 1]

l3 = [0, 52, 102, 155]
l3_err = [1, 1, 1, 1]

l4 = [0, 49, 97, 145, 193]
l4_err = [1, 1, 1, 1, 1]

l5 = [0, 43, 87, 130, 174]
l5_err = [1, 1, 1, 1, 1]


coef1 = np.polyfit(i_1, l1, 1)
poly1d_fn1 = np.poly1d(coef1)  # to create a linear function with coefficients

coef2 = np.polyfit(i_1, l2, 1)
poly1d_fn2 = np.poly1d(coef2)  # to create a linear function with coefficients

coef3 = np.polyfit(i_1, l3, 1)
poly1d_fn3 = np.poly1d(coef3)  # to create a linear function with coefficients

coef4 = np.polyfit(i_2, l4, 1)
poly1d_fn4 = np.poly1d(coef4)  # to create a linear function with coefficients

coef5 = np.polyfit(i_2, l5, 1)
poly1d_fn5 = np.poly1d(coef5)  # to create a linear function with coefficients

plt.plot(i_1, poly1d_fn1(i_1), color ='red')
plt.errorbar(i_1, l1, yerr = l1_err, fmt ='.', color ='black')

plt.plot(i_1, poly1d_fn2(i_1), color ='lime')
plt.errorbar(i_1, l2, yerr = l2_err, fmt ='.', color ='black')

plt.plot(i_1, poly1d_fn3(i_1), color ='blue')
plt.errorbar(i_1, l3, yerr = l3_err, fmt ='.', color ='black')

plt.plot(i_2, poly1d_fn4(i_2), color ='cyan')
plt.errorbar(i_2, l4, yerr = l4_err, fmt ='.', color ='black')

plt.plot(i_2, poly1d_fn5(i_2), color ='magenta')
plt.errorbar(i_2, l5, yerr = l5_err, fmt ='.', color ='black')

plt.legend(['2204 Hz', '2402 Hz', '2600 Hz', '2802 Hz', '3095 Hz'])

plt.savefig('PIC_3.png', dpi = 1200)
plt.close(fig)

p, V = np.polyfit(i_1, l1, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_1, l2, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_1, l3, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_2, l4, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))

p, V = np.polyfit(i_2, l5, 1, cov=True)
print("slope: {} +/- {}".format(p[0], np.sqrt(V[0][0])))
print("intercept: {} +/- {}".format(p[1], np.sqrt(V[1][1])))
