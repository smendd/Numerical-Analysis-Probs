# Use (1.21) to approximate the root of f(x) = (x-1)(x-2)(x-3)(x-4)-(10e-6)x^6 near r = 4
# Find the error magnification factor. Use fzero (fsolve) to check your approximation
from scipy.optimize import fsolve

def f(x):
    x = float(x)
    return (x-1)*(x-2)*(x-3)*(x-4)

def df(x):
    x = float(x)
    return 4*(x**3) - 30*(x**2) + 70*x - 50

def g(x):
    x = float(x)
    return x**6

w = 10e-6
def actual_f(x):
    x = float(x)
    return (x-1)*(x-2)*(x-3)*(x-4) - w*(x**6)

approx_root = fsolve(f,4.0)
print("Approximate root: " + str(approx_root))

error_mag_factor = abs(g(approx_root))/abs(approx_root*df(approx_root)) # type: ignore
print("Error Magnification Factor: " + str(error_mag_factor))

actual_root = fsolve(actual_f,4.0)
print("Actual root: " + str(actual_root))
