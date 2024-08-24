
import math

def f(theta, L_1 = 2, L_2 = math.sqrt(2), L_3 = math.sqrt(2), gamma = math.pi/2, p_1 = math.sqrt(5), p_2 = math.sqrt(5), p_3 = math.sqrt(5), x_1 = 4, x_2 = 0, y_2 = 4):
    A_2 = L_3*math.cos(theta) - x_1
    B_2 = L_3*math.sin(theta)
    A_3 = L_2*(math.cos(theta)*math.cos(gamma) - math.sin(theta)*math.sin(gamma)) - x_2
    B_3 = L_2*(math.cos(theta)*math.sin(gamma) + math.sin(theta)*math.cos(gamma)) - y_2
    N_1 = B_3*(p_2**2 - p_1**2 - A_2**2 - B_2**2) - B_2*(p_3**2 - p_1**2 - A_3**2 - B_3**2)
    N_2 = -A_3*(p_2**2 - p_1**2 - A_2**2 - B_2**2) + A_2*(p_3**2 - p_1**2 - A_3**2 - B_3**2)
    D = 2*(A_2*B_3 - B_2*A_3)
    return N_1**2 + N_2**2 - (p_1**2)*(D**2)

