# Apply fixed point iteration to find the soln of each equation to eight correct decimal places
import numpy as np

def g(x):
    return (2*x + 2)**(1/3)


x = 0.5
i = 20
for j in range(0,i):
    x_1 = g(x)
    x = x_1
    print("Step: " + str(j+1) + " | x: " + str(x))


