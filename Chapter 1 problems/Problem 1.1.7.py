# Use the bisection method to find the two real numbers x, within six correct decimal places,
# that make the determinant of the matrix A equal to 1000.
# For each solution you find, test it by computing the corresponding determinant and reporting 
# how many correct decimal places the determinant has when your solution x is used.
import numpy as np
import matplotlib.pyplot as plt


# Investigating where the solutions approximately are by testing different values for x
spaces = np.linspace(-20,12,100)
for x in spaces:
    m = np.array([[1, 2, 3, x], [4, 5, x, 6], [7, x, 8, 9], [x, 10, 11, 12]])
    det_m = np.linalg.det(m)
    #print(x, det_m)

# After some investigation, we will set our starting intervals at [9,10], and [-18,-17]

def A(x):
    return np.array([[1, 2, 3, x], [4, 5, x, 6], [7, x, 8, 9], [x, 10, 11, 12]])

def g(x):
    return np.linalg.det(A(x)) - 1000

# Using the bisection method
intervals = [(9,10),(-18,-17)]
for i in intervals:
    a,b = i
    while float(b-a)/2 > 1e-7:
        c = float(a+b)/2
        if g(c) == 0:
            break
        elif g(a)*g(c) < 0:
            b = c
        else:
            a = c
    print("The approx. solution is " + str(float(a+b)/2))
    print("Approx determinant: " + str(np.linalg.det(A(float(a+b)/2))))

    # Looks like both solutions have 4 and 3 decimal places correct, respectively
