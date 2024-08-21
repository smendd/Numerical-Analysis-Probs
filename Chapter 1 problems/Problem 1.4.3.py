# Apply Newton's Method to find the only root to as much accuracy as possible, 
# and find the roots multiplicity. Then use Modified Newtons Method to converge to the root quadratically
# Report the forward and backward errors of the best approx obtained from each method

def f(x):
    x = float(x)
    return 27*(x**3) + 54*(x**2) + 36*x + 8

def df(x):
    x = float(x)
    return 81*(x**2) + 108*x + 36


nm_root = 1
for n in range(1,44):
    x_i = nm_root - (f(nm_root))/(df(nm_root))
    print("Step: " + str(n) + " | Newton's Method Approx: " + str(x_i))
    nm_root = x_i 

FE = abs((2/float(3)) - nm_root)
BE = abs(f(nm_root))

# After investigating using wolfram, we find that this root has multiplicity m = 3
m = 3
modnm_root = 1
for n in range(1,4):
    x_i = modnm_root - (m*f(modnm_root))/(df(modnm_root))
    print("Step: " + str(n) + " | Modified Newton's Method Approx: " + str(x_i))
    modnm_root = x_i 

modFE = abs((2/float(3)) - modnm_root)
modBE = abs(f(modnm_root))

print("Newton Method FE: " + str(FE) + "\n" +
      "Modified Newton Method FE: " + str(modFE) + "\n" +
      "Newton Method BE: " + str(BE) + "\n" +
      "Modified Newton Method BE: " + str(modBE))
