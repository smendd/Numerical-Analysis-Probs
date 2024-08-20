# Use (1.21) to approximate the root near 3 of f(x) = (1+w)x^3-3x^2+x-3 for a constant w
from scipy.optimize import fsolve

def f(x):
    x = float(x)
    return x**3 - 3*(x**2) + x - 3

def df(x):
    x = float(x)
    return 3*(x**2) - 6*x +1

def g(x):
    x = float(x)
    return x**3


approx_root = fsolve(f,3.0)
print(approx_root)
# the approximate root is 3.0


# Setting w = 10e-3, find the actual root and compare with part a
w = 10e-3
def exact_f(x):
    x = float(x)
    return (1+w)*(x**3) - 3*(x**2) + x - 3

actual_root = fsolve(exact_f,3)
print(actual_root)
# the actual root is about 2.97

delta_r = -(w*g(3))/(df(3))
print(delta_r)
print(actual_root[0] - 3.0)

# when we calculate the theoretical delta r and compare with the actual delta r, we can see that they are very close
