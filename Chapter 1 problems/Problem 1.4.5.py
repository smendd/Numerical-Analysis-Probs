# A silo composed of a right circular cylinder of height 10m surmounted by a hemispherical dome
# contains 400m^3 of volume. Find the base radius of the silo to four correct decimal places
import sympy as sp

r = sp.symbols('r')
expr = 2*sp.pi*(r**3) + 10*sp.pi*(r**2) - 400
f = sp.lambdify(r,expr)
dfexpr = sp.diff(expr)
df = sp.lambdify(r,dfexpr)

r_0 = 4
TOL = 1e-4
diff = 1
step = 1
while diff > TOL:
    r_i = r_0 - (f(r_0))/(df(r_0))
    print('Step: ' + str(step) + ' | Approx: ' + str(r_i))
    step += 1
    diff = abs(r_i - r_0)
    r_0 = r_i
