"""fitLines.py -- Fitting peaks from a 152Eu gamma source
Final project solution for 2019 REU 

@author: NAME
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#from scipy.constants import h,k,c #useful for blackbody radiation data

    
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x-mu)**2/(2*sigma*sigma))

def lin(x, d, e):
    return d*x + e

def poly(x, d, e, f, g):
    return d*x**3 + e*x**2 + f*x + g



if __name__=='__main__':
    lines_filename = '152Eu_lines.txt'
    data_filename = '152Eu_data.dat'
    