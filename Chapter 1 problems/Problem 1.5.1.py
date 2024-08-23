# Use the secant method to find the solution of each equation to exercise 1
import math
def f(x:float):
    return math.e**x + math.sin(x) - 4 # Change the function to solve the other equations

x_0, x_1 = 1, 2
TOL = 1e-7
diff = 1
step = 1
while diff > TOL:
    x_i = x_1 - (f(x_1)*(x_1 - x_0))/(f(x_1) - f(x_0))
    print("Step: " + str(step) + " | Approx: " + str(x_i))
    diff = abs(x_i - x_1)
    step += 1
    x_0 = x_1
    x_1 = x_i

