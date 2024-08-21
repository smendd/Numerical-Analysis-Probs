# Each equation has one root. Use Newton's Method to approx. the root to eight correct decimal places
import math

# Redefine f and df depending on the equation you're working with, you can also use this for 1.4.2
def f(x):
    x = float(x)
    return x**5 + x - 1

def df(x):
    x = float(x)
    return 5*(x**4) + 1

x = 1
for n in range (1,9):
    x_i = x - (f(x))/(df(x))
    print("Step: " + str(n) + " Approx: " + str(x_i))
    x = x_i 
