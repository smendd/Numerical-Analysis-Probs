# Use the method of false position to find the solution of each equation in exercise 1
import math
def f(x:float):
    return math.e**x + math.sin(x) - 4 # Change this function to solve the others in the problem

a,b = 1,2
TOL = 1e-7
diff = 1
step = 1
while diff > TOL:
    c = (b*f(a) - a*f(b))/(f(a) - f(b))
    if f(c) == 0:
        break
    elif f(a)*f(c) < 0:
        b = c
    else:
        a = c
    print("Step: " + str(step) + " | Approx: " + str(c))
    step += 1
    diff = abs(f(c) - 0.0)


