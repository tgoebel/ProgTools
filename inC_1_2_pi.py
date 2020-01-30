# -*- coding: utf-8 -*-
#! python3.7
"""
    - compute pi using Leibinz scheme
    for n= 10, 50, 100, 1000
    compare to numpy.pi
"""
#======================================
#           modules
#======================================
import numpy as np
#import matplotlib.pyplot as plt
#------------my fcts.------------------
def fct_my_pi( n):
    f_sum_pi = 0
    for k in range( n):
        f_sum_pi += 1./(( 4*k+1)*( 4*k+3) )
    return 8*f_sum_pi
#======================================
#           parameters
#======================================
# test leibniz precision for this no. of iterations
a_n = np.array([10, 50, 100, 1000])
#======================================
#           compute pi
#======================================
for n in a_n:
    # compute pi using Leibniz
    f_my_pi = fct_my_pi( n) 
    # compare value to numpy.pi
    f_err = abs( f_my_pi - np.pi)
    print( 'pi-error (for n=%i iterations): %10.8f'%(n, f_err))







