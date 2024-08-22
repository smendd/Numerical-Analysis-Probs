import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols('x')
expr = sp.exp(sp.sin(x)**3) + x**36 - 2*x**4 - x**3 - 1
f = sp.lambdify(x,expr)
dfexpr = sp.diff(expr)
df = sp.lambdify(x,dfexpr)


xs = np.linspace(-1,1,100)
ys = [f(i) for i in xs]
#plt.plot(xs,ys)
#plt.grid()
#plt.show()

#there is a root near x = -1.25, 0.1, 1.6

x_0 = [-1.25,0.1,1.6]
exact_roots = [-1.19762372213356, 0, 1.53013350816661]
TOL = 1e-7

for i in range(len(x_0)):
    err = 1
    step = 0
    e_prev = 1
    e_i = abs(x_0[i] - exact_roots[i])
    print('ROOT ' + str(i))
    print(str(step) + '\t|\t' + str(x_0[i]) + '\t|\t' + str(e_i) + '\t')
    while err > TOL:
        x_i = x_0[i] - f(x_0[i])/df(x_0[i])
        err = abs(x_i - x_0[i])
        x_0[i] = x_i
        e_i = abs(x_0[i] - exact_roots[i])
        step += 1
        err_growth = e_i/(e_prev**2)
        print(str(step) + '\t|\t' + str(x_0[i]) + '\t|\t' + str(e_i) + '\t|\t' + str(err_growth))
        e_prev = e_i


# The roots at -1.011 and 1.024 converge quadratically while the one at zero converges linearly
func = sp.lambdify(x, sp.diff(expr,x,4))
print(func(0))
# after looking, we find that the multiplicity of the root at x = 0 is 4
