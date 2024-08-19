# Is g(x) = (cos^2)(x) convergent? Find the fixed point to six correct decimal places,
# report the number of FPI steps needed. Discuss local convergence using Theorem 1.6
import math

def g(x):
    return (math.cos(x)**2)

# after some hand calculation, we will set our initial guess to be r = 0.39
# as this number satisfies |g'(r)| < 1

x = 0.39
diff = 2
TOL = 5e-7
i = 0
while abs(diff) > TOL:
    x_1 = g(x)
    diff = x_1 - x
    x = x_1
    print("Step: " + str(i+1) + " | x: " + str(x))
    i += 1

# we see that we need 312 steps for six correct decimal places