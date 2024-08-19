# Calculate the square roots of the following numbers (3, 5) to eight correct decimal places by using FPI
# State your initial guess and the number of steps needed
import math

def g(x):
    y = float(x)
    return (y + 3/y)/2

x = 1
for i in range(0,5):
    x_1 = g(x)
    x = x_1
    print("Step: " + str(i+1) + " | x: " + str(x))

# We needed 5 steps for both sqrt(5) and sqrt(3) at starting guess x = 1    

