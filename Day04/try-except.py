# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:39:49 2019

try-except statement example

REU CMP Class June 2019
@author: Chris
"""

try:
    import numpy as np
except Exception as e:
    print("numpy is not installed!", e)
else:
    #"The else block will excecute if try is successful"
    print('numpy version:', np.__version__ )

  
try:
    import nonexistentmodule
except Exception as e:
    print('\nAny exception that occurs is handled by the `try-except` structure',
           'instead of crashing your code.\nException:', e)
else:
    print("The else block will excecute if 'try' doesn't throw an error")
finally:
    print("\n'finally' is always executed before leaving the try statement.")


#uncomment the line below to attempt an import without the try-except statements
#import nonexistentmodule