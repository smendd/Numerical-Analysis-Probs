# Use the Bisection Method to calculate the solution of cosx = sinx in the interval [0,1] within six correct decimal places
import math

def g(n):
    return math.cos(n) - math.sin(n)

# Using the bisection method
a,b = 0,1
while float((b - a))/2 > 1e-7:
        c = float((a+b))/2
        if g(c) == 0:
            break
        elif g(a)*g(c) < 0:
            b = c
        else:
            a = c
        print("Approx. solution: " + str((float(a+b))/2))