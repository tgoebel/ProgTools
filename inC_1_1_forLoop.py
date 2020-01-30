# -*- coding: utf-8 -*-
#!python3.7
"""
    - compute sum using a for loop
     
    x = sum( 5*i), for i=0 to n
"""
#======================================
#           modules
#======================================
import numpy
#------------my fcts.------------------
def my_sum( n):
    x = 0
    for i in range( n):
        #x = x + 5*i
        x += 5*i
        #print( x)
    return x
#======================================
#           parameters, variables
#======================================
n = 2


#======================================
#          compute sum
#======================================
x = my_sum( n)

print( 'final value of sum', x)









