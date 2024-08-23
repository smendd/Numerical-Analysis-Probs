# Use inverse quadratic interpolation to find the solution of each equation in exercise 1
import math
def f(x:float):
    return math.e**x + math.sin(x) - 4 # Change this function to solve the other equations

x_0, x_1 ,x_2 = 1,2,0
step = 1
diff = 1
TOL = 1e-7
while diff > TOL:
    q = (f(x_0))/(f(x_1))
    r = (f(x_2))/(f(x_1))
    s = (f(x_2))/(f(x_0))
    x_3 = x_2 - (r*(r-q)*(x_2 - x_1) + (1-r)*s*(x_2 - x_0))/((q-1)*(r-1)*(s-1))
    print("Step: " + str(step) + " | Approx: " + str(x_3))
    diff = abs(x_3 - x_2)
    step += 1
    x_0 = x_1
    x_1 = x_2
    x_2 = x_3