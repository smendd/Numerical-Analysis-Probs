# Calculate the square roots of the following numbers to eight correct decimal places
# by using the bisection method to solve x^2 - A = 0 where A is 2,3,5. 
# State your starting interval and the number of steps needed

# We can solve problem 1.1.5 by changing g to be a cubic function in line 13

# We'll use the same program and tweak a few variables to solve for all three values of A
# For A = 2, we use the starting interval of (1,1.5), we find that we need 26 steps
# For A = 3, we use the interval (1.5,2), and we find that we need 28 steps
# for A = 5, we use the interval (2,2.5), and we find that we need 26 steps
A = 5
def g(n):
    return n**2 - A

a,b = 2,2.5
steps = 1
while float((b - a))/2 > 1e-8:
        c = float((a+b))/2
        if g(c) == 0:
            break
        elif g(a)*g(c) < 0:
            b = c
        else:
            a = c
        steps += 1
        print("Step: " + str(steps) + " | Approx. Root: " + str((float(a+b))/2))
