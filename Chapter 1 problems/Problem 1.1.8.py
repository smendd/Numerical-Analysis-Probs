# Let A denote the 5x5 Hilbert matrix. Its largest eigval is about 1.567
# Use the bisection method to decide how to change the upper left entry to make the largest eigenvalue of A equal to pi
# Determine A_1,1 within 6 correct decimal places. 
import numpy as np
from scipy.linalg import hilbert
import math

A = hilbert(5)

def g(x):
    A[0][0] = x
    eigvals = np.linalg.eigvals(A)
    max_eig = max(eigvals)
    return max_eig - math.pi

# after some investigating, we will start with an initial interval of [1,4]
a,b = float(1),float(4)
while (b-a)/2 > 1e-6:
    c = (a+b)/2
    if g(c) == 0:
        break
    elif g(a)*g(c) < 0:
        b = c
    else:
        a = c
print("A_1,1 = " + str((a+b)/2))