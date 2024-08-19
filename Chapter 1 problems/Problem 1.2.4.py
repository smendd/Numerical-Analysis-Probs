# Calculate the cube roots of the following numbers to eight correct decimal places using FPI
# where A = 2,3,5. State your initial guess and the number of steps needed.

A = 5
def g(x):
    y = float(x)
    return (2*y + A/(y**2))/3

x = 1   # We'll use 1 as our initial guess for all three cases
for i in range(0,6):
    x_1 = g(x)
    x = x_1
    print("Step: " + str(i+1) + " | x: " + str(x))

# We need 5 steps for cube root of 2
# 5 steps for cube root of 3
# 6 steps for cube root of 5