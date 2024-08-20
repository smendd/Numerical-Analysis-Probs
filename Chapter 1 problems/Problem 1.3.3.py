# use fzero (brentq) to find the root of f(x) = 2xcosx - 2x + sinx^3 on [-0.1,0.2]
# report the forward and backward errors
import scipy.optimize as sp
from scipy.misc import derivative
import numpy as np
import math

def f(x):
    x = float(x)
    return (2*x*math.cos(x)) - 2*x + math.sin(x**3)

a,b = -0.1,0.2
root_brentq = sp.brentq(f,a,b)
FE_brentq = abs(0.0 - root_brentq) # type: ignore
BE_brentq = abs(f(root_brentq))
print("Brentq Root: " + str(root_brentq) + " Forward error: " + str(FE_brentq) + " Backwards error: " + str(BE_brentq))

# Run the bisection method with initial interval [-0.1,0.2] to find as many correct digits as possible and report your conclusion
root_bisec = sp.bisect(f,a,b)
FE_bisec = abs(0.0 - root_bisec) # type: ignore
BE_bisec = abs(f(root_bisec))
print("Bisection root: " + str(root_bisec)+ " Forward error: " + str(FE_bisec) + " Backwards error: " + str(BE_bisec))

# the brentq root has a larger forward error than the bisection root, but the backwards errors are pretty close
