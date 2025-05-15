import numpy as np 


tc = 0.12
Dy = 26 * tc
clmax = 1.61

V = 150/3.6 #m/s
rho = 1.225 #kg/m^3
S = 14.14 
W = 21000 #N

q = 0.5 * rho * V**2

n = q * clmax / (W/S)
print("n = ", n)
