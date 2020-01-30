# -*- coding: utf-8 -*-
#python3.7
"""
- find all divisors between 2 and 9 for any integer number
"""
#======================================
#           modules
#======================================
import numpy as np
#------------my fct--------------------
def fct_find_divisor( i_n):
    a_testDiv = np.arange( 2, 10, 1)
    l_trueDiv = []
    for curr_div in a_testDiv:
        #print( curr_div, i_n%curr_div)
        if i_n%curr_div == 0:
            l_trueDiv.append( curr_div)
    return l_trueDiv

def fct_checkIfInt( number):
    """ check if number is integer """
    try:
        int( number)
        return int( number)
    except ValueError:
        s_error = "number is not an integer, %s"%( type( number))
        raise( ValueError( s_error))
    
#======================================
#           params, variables
#======================================
#i_Number = 27
# take number for user
i_Number = input( "Provide Integer Number: ")
# check if input is integer
i_Number = fct_checkIfInt( i_Number)
#======================================
#           computation
#======================================
print( 'all divisors of %i :'%(i_Number), fct_find_divisor( i_Number) )







