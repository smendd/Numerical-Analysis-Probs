# Let f(x) = sinx^3 - x^3
from scipy.optimize import fsolve
import math

def f(x):
    y = float(x)
    return math.sin(y**3) - (y**3)

# Find the multiplicity of the root r = 0
# Hand calculating the multiplicity at r = 0 gives a multiplicity of nine


# Locate a root with initial guess x = 0.1 and fzero (the textbook uses matlab but I will use scipy's fsolve)
# What are the forward and backward errors of fsolve's response?
root_array = fsolve(f, 0.1)
root = root_array[0]

FE = abs(0 - root)
BE = abs(f(root))
print("Forward error: " + str(FE) + " Backwards error: " + str(BE))

