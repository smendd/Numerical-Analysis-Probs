# Use the bisection method to find the root to six/eight correct decimal places 
# You can plug in any function for g, and pick the starting interval a,b manually
# to change the accuracy to more decimal places, change the tolerance in line 10
import math

def g(x):
    return math.log(x) + x**2 - 3

a,b = 0.5,2
while (b-a)/2 > 0.000000001:
    c = (a+b)/2
    if g(c) == 0:
        break
    elif g(a)*g(c) < 0:
        b = c
    else:
        a = c

print("The inverval (" + str(a) + ", " + str(b) + ") contains a root")
print("The approximate root is " + str((a+b)/2))

