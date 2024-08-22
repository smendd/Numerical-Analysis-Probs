# A 10cm high cone contains 60cm^3 of ice cream, including a hemispherical scoop on top
# Find the radius of the scoop to four decimal places
import sympy as sp

r = sp.symbols('r')
expr = 2*sp.pi*(r**3) + (10/3)*sp.pi*(r**2) - 60
f = sp.lambdify(r,expr)
dfexpr = sp.diff(expr)
df = sp.lambdify(r,dfexpr)

r_0 = 1
TOL = 1e-4
diff = 1
step = 1
while diff > TOL:
    r_i = r_0 - (f(r_0))/(df(r_0))
    print('Step: ' + str(step) + ' | Approx: ' + str(r_i))
    step += 1
    diff = abs(r_i - r_0)
    r_0 = r_i
