# -*- coding: utf-8 -*-
# python3.7
"""
    - find max. of function:
        y = v0*t - 0.5*g*t**2

"""
#======================================
#           modules
#======================================
import numpy as np
import matplotlib.pyplot as plt
#------------my fct--------------------


#======================================
#           parameters
#======================================
v0 = 2 # m/s
g  = 9.81 # m/s2
i_n= 2000
a_t= np.linspace( 0, 2, i_n)
#======================================
#           compute max.
#======================================
# compute height at each t
a_y = v0*a_t - 0.5*g*a_t**2
# compare neighboring values, find max
for i in range( 1, i_n, 1):
    if a_y[i] > a_y[i-1]:
        f_ymax = a_y[i]
        f_tmax = a_t[i]
    else:
        break
print( "max height: %.3f m"%( f_ymax), "t at ymax= %.4f"%( f_tmax))

i = 1
while a_y[i] > a_y[i-1]:
    f_ymax2 = a_y[i]
    f_tmax2 = a_t[i]
    i += 1
    
print( "max height: %.3f m"%( f_ymax2), "t at ymax= %.4f"%( f_tmax2))
#======================================
#           plot trajectory
#======================================
plt.figure( 1)
plt.plot( a_t, a_y, 'b-')
plt.plot( [f_tmax], [f_ymax], 'r*')
plt.xlabel( 'Time [s]')
plt.ylabel( 'Height of Object [m]')
plt.show()

# plt.savefig( 'test.png')  
















