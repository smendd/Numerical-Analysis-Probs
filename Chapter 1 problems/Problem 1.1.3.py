# Use the bisection method to locate all solutions of the following equations.
# Sketch the function and identify three intervals of length one that contain a root.
# Find the roots to six correct decimal places.

import matplotlib.pyplot as plt
import numpy as np

def g(n):
    return 2*(n**3) - 6*n - 1

# Inspecting where the approximate solutions are by sketching g
x = np.linspace(-2,2,40)
y = [i for i in g(x)]

#plt.plot(x,y)
#plt.grid()
#plt.show()

# From the graph we see there is a root between [-2.5, -1.5],[-0.5, 0.5],[1.5,2.5]
# Using the bisection method on the three intervals
intervals = [(-2,-1), (-1,0), (1,2)]
for i in intervals:
    a,b = i
    while float((b - a))/2 > 1e-7:
        c = float((a+b))/2
        if g(c) == 0:
            break
        elif g(a)*g(c) < 0:
            b = c
        else:
            a = c
    print("Approximate Root: " + str((a+b)/2))

