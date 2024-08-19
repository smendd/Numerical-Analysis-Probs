# Derive 3 different g(x) for finding roots to six correct decimal places by FPI
# Run FPI for each g(x) and report results, convergence or divergence
# Derive more g(x) until all roots are found. For each convergent run, determine the value
# of S from the errors and compare with S determined from calculus.

import matplotlib.pyplot as plt
import numpy as np
# f(x) = 2x^3 - 6x -1

def f(x):
    y = float(x)
    return 2*(x**3) - 6*x - 1

#xs = np.linspace(-3,3,50)
#ys = [f(i) for i in xs]
#plt.plot(xs,ys)
#plt.grid()
#plt.show()


def g_1(x):
    y = float(x)
    return (2*(y**3) - 1)/6

def g_2(x):
    y = float(x)
    return ((1 + 6*y)/2)**(1/float(3))

def g_3(x):
    y = float(x)
    return 1/(2*(x**2) - 3)

x = 1
for i in range(0,20):
    x_1 = g_1(x)
    e_i = abs(-0.168254 - x)
    e_i1 = abs(-0.168254 - x_1)
    x = x_1
    print("Step: " + str(i+1) + " | x: " + str(x) + " | S error: " + str(e_i1/e_i))

# This FPI works when x = 1 initial guess, converges to x = -0.168254, but doesnt 
# work for large x

x = 1
for i in range(0,20):
    x_1 = g_2(x)
    e_i = abs(1.810037 - x)
    e_i1 = abs(1.810037 - x_1)
    x = x_1
    print("Step: " + str(i+1) + " | x: " + str(x) + " | S error: " + str(e_i1/e_i))

# This works for x = 1 initial guess, converges to 1.810037, but doesnt work for negative numbers

x = -1.3
for i in range(0,20):
    x_1 = g_3(x)
    e_i = abs(-0.366025 - x)
    e_i1 = abs(-0.366025 - x_1)
    x = x_1
    print("Step: " + str(i+1) + " | x: " + str(x) + " | S error: " + str(e_i1/e_i))

# gives a root at x = -0.36602540
