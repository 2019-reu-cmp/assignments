# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:44:19 2019

arbitrary prescision

@author: Chris
"""

from mpmath import mp

mp.dps = 100 #set prescision (number of digits)
pi = mp.mpf( mp.pi ) #mpmath has a good built in pi

pi_string = '3.1415926535897932384626433832795028841971693993751058209749445923078164062'
print( len(pi_string),' digits of pi')
#mpf input should be a string, entering a float is imprecise
pi2 = mp.mpf(pi_string)
difference = mp.fsub(  pi2, pi ) 
digits_to_print = mp.dps-len(pi_string) #number of sig. figs. to print
print( 'difference: ', end='')
mp.nprint( difference , n=digits_to_print ) #need nprint for mpf truncation


import decimal as de
de.getcontext().prec = 50 #set prescision for decimal module

pi_de=de.Decimal(pi_string)
### uncomment below
#print('decimal pi', pi_de)
#print('1/pi', 1/pi_de)