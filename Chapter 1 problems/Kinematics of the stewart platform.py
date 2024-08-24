# Write a function file for f(theta). The parameters L1, L2, L3, gamma, x1,x2,y2 are fixed constants and the strut lengths
# p1,p2,p3 will be known for a given pose.
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Kinematics_function import f

# Plot f(theta) on [-pi,pi], as a check, there should be roots at +- pi/4

#plots f(theta) on [-pi,pi]
xs = np.linspace(-math.pi,math.pi,100)
ys = [f(i) for i in xs]
#plt.plot(xs,ys)
#plt.scatter([-math.pi/4, math.pi/4],[0,0])
#plt.grid()
#plt.show()

# reproduce figure 1.15. In addition, draw the struts
#fig,(ax1,ax2) = plt.subplots(1,2)

#ax1.plot([1,2,2,1],[2,1,3,2])
#ax1.scatter([0,4,0],[0,0,4])
#ax1.plot([0,2],[4,3])
#ax1.plot([0,1],[0,2])
#ax1.plot([2,4],[1,0])

#ax2.plot([1,3,2,1],[2,2,1,2])
#ax2.scatter([0,4,0],[0,0,4])
#ax2.plot([0,2],[0,1])
#ax2.plot([0,1],[4,2])
#ax2.plot([3,4],[2,0])

#plt.show()

# Solve the forward kinematics problem for the planar Stewart platform specified by
# x_1 = 5, (x_2,y_2) = (0,6), L_1 = L_3 = 3, L_2 = 3sqrt(2), gamma = pi/4, p_1 = p_2 = 5, p_3 = 3

f_args = (3, 3*math.sqrt(2), 3, math.pi/4, 5, 5, 3, 5, 0, 6)


# Code to find bracketing intervals for all roots
xs = np.linspace(-math.pi,math.pi,500)
ys = [f(i,L_1=3,L_2 = 3*math.sqrt(2),L_3=3,gamma=math.pi/4,p_1=5,p_2=5,p_3=3,x_1=5,x_2=0,y_2=6) for i in xs]
#plt.plot(xs,ys)
#plt.grid()
#plt.show()

# Obtains the roots of f using brentq
list_ab = [(-0.8,-0.6),(-0.4,-0.2),(1.1,1.2),(2.1,2.15)]
roots = []
for pair in list_ab:
    a,b=pair
    root = sp.optimize.brentq(f,a,b,args=f_args)
    roots.append(root)

# Obtains the corresponding x,y pairs from each root theta
def get_xy(theta, L_1 = 2, L_2 = math.sqrt(2), L_3 = math.sqrt(2), gamma = math.pi/2, p_1 = math.sqrt(5), p_2 = math.sqrt(5), p_3 = math.sqrt(5), x_1 = 4, x_2 = 0, y_2 = 4):
    A_2 = L_3*math.cos(theta) - x_1
    B_2 = L_3*math.sin(theta)
    A_3 = L_2*(math.cos(theta)*math.cos(gamma) - math.sin(theta)*math.sin(gamma)) - x_2
    B_3 = L_2*(math.cos(theta)*math.sin(gamma) + math.sin(theta)*math.cos(gamma)) - y_2
    N_1 = B_3*(p_2**2 - p_1**2 - A_2**2 - B_2**2) - B_2*(p_3**2 - p_1**2 - A_3**2 - B_3**2)
    N_2 = -A_3*(p_2**2 - p_1**2 - A_2**2 - B_2**2) + A_2*(p_3**2 - p_1**2 - A_3**2 - B_3**2)
    D = 2*(A_2*B_3 - B_2*A_3)
    return (N_1/D,N_2/D)

xy_pairs = []
for r in roots:
    xy_pairs.append(get_xy(r,L_1=3,L_2 = 3*math.sqrt(2),L_3=3,gamma=math.pi/4,p_1=5,p_2=5,p_3=3,x_1=5,x_2=0,y_2=6))


# Graphs all four poses
#fig, axs = plt.subplots(2,2)
L_2 = 3*math.sqrt(2)
L_3= 3
gamma= math.pi/4
p_1= 5
p_2= 5
p_3= 3
x_1= 5
x_2= 0
y_2= 6
#for i, ax in enumerate(axs.flatten()):
    #x = xy_pairs[i][0]
    #y = xy_pairs[i][1]
    #theta = roots[i]
    #ax.plot([x,x + L_2*math.cos(theta + gamma), x + L_3*math.cos(theta), x],
    #        [y, y + L_2*math.sin(theta + gamma), y + L_3*math.sin(theta),y])
    #ax.scatter([0,x_1,x_2],[0,0,y_2])
    #ax.plot([0,x],[0,y])
    #ax.plot([x_2, x+ L_2*math.cos(theta + gamma)],
    #        [y_2, y + L_2*math.sin(theta+gamma)])
    #ax.plot([x_1,x+L_3*math.cos(theta)],
    #        [0,y+L_3*math.sin(theta)])
    
#plt.show()

# checks that the strut lengths match the p values
for i in range(4):
    x = xy_pairs[i][0]
    y = xy_pairs[i][1]
    theta = roots[i]
    strut_lengths = []
    ps = [p_1,p_2,p_3]
    strut_lengths.append(math.sqrt((x-0)**2 + (y-0)**2))
    strut_lengths.append(math.sqrt((x_1 - (x + L_3*math.cos(theta)))**2 + (0 - (y+L_3*math.sin(theta)))**2))
    strut_lengths.append(math.sqrt((x_2 - (x + L_2*math.cos(theta+gamma)))**2 + (y_2 - (y + L_2*math.sin(theta+gamma)))**2))
    for j in range(3):
        print("p: " + str(ps[j]) + " | Strut Length: " + str(strut_lengths[j]))


# Change strut length to p_2 = 7 and resolve the problem, for these parameters there are six poses

# the code here is pretty much the same as part 4
part5_xs = np.linspace(-math.pi,math.pi,500)
part5_ys = [f(i,L_1=3,L_2 = 3*math.sqrt(2),L_3=3,gamma=math.pi/4,p_1=5,p_2=7,p_3=3,x_1=5,x_2=0,y_2=6) for i in part5_xs]
#plt.plot(part5_xs,part5_ys)
#plt.grid()
#plt.show()

part5_list_ab = [(-0.7,-0.6),(-0.4,-0.3),(0,0.1),(0.4,0.5),(0.8,1.2),(2.4,2.6)]
part5_roots = []
part5_f_args = (3, 3*math.sqrt(2), 3, math.pi/4, 5, 7, 3, 5, 0, 6)
for pair in part5_list_ab:
    a,b=pair
    root = sp.optimize.brentq(f,a,b,args=part5_f_args)
    part5_roots.append(root)

part5_xy_pairs = []
for r in part5_roots:
    part5_xy_pairs.append(get_xy(r,L_1=3,L_2 = 3*math.sqrt(2),L_3=3,gamma=math.pi/4,p_1=5,p_2=7,p_3=3,x_1=5,x_2=0,y_2=6))


#fig, axs = plt.subplots(2,3)
L_2 = 3*math.sqrt(2)
L_3= 3
gamma= math.pi/4
p_1= 5
p_2= 7
p_3= 3
x_1= 5
x_2= 0
y_2= 6

#for i, ax in enumerate(axs.flatten()):
#    x = part5_xy_pairs[i][0]
#    y = part5_xy_pairs[i][1]
#    theta = part5_roots[i]
#    ax.plot([x,x + L_2*math.cos(theta + gamma), x + L_3*math.cos(theta), x],
#            [y, y + L_2*math.sin(theta + gamma), y + L_3*math.sin(theta),y])
#    ax.scatter([0,x_1,x_2],[0,0,y_2])
#    ax.plot([0,x],[0,y])
#    ax.plot([x_2, x+ L_2*math.cos(theta + gamma)],
#            [y_2, y + L_2*math.sin(theta+gamma)])
#    ax.plot([x_1,x+L_3*math.cos(theta)],
#            [0,y+L_3*math.sin(theta)])
    
#plt.show()

#for i in range(6):
#    x = part5_xy_pairs[i][0]
#    y = part5_xy_pairs[i][1]
#    theta = part5_roots[i]
#    part5_strut_lengths = []
#    part5_ps = [p_1,p_2,p_3]
#    part5_strut_lengths.append(math.sqrt((x-0)**2 + (y-0)**2))
#    part5_strut_lengths.append(math.sqrt((x_1 - (x + L_3*math.cos(theta)))**2 + (0 - (y+L_3*math.sin(theta)))**2))
#    part5_strut_lengths.append(math.sqrt((x_2 - (x + L_2*math.cos(theta+gamma)))**2 + (y_2 - (y + L_2*math.sin(theta+gamma)))**2))
#    for j in range(3):
#        print("p: " + str(part5_ps[j]) + " | Strut Length: " + str(part5_strut_lengths[j]))

# Find a strut length p_2, with the rest of the parameters as in step 4, for which there are only two poses
part6_xs = np.linspace(-math.pi,math.pi,500)
part6_ys = [f(i,L_1=3,L_2 = 3*math.sqrt(2),L_3=3,gamma=math.pi/4,p_1=5,p_2=4,p_3=3,x_1=5,x_2=0,y_2=6) for i in part6_xs]
plt.plot(xs,ys)
plt.grid()
plt.show()
# when p_2 = 4, we get only two poses


