'''
Processing .csv output from Lumerical FDTD Solution 

Author : Mark S. Brown
Started : 16th Jan 2014

Description : In this module we will collect functions for loading, processing
and plotting data generated by Lumerical
'''

from __future__ import division,print_function
import re
import os
from pandas import Series

def parsefilename(fn, verbose=0):
    '''
    Splits given filename generated by _pylumerical.py_ into pandas Series objects
    '''

    try:
        variables, csvtype = fn.split('.fsp')
    except ValueError:
        variables = fn
        csvtype = "none"
    
    return dict(param.split('=') for param in variables.split('_'))

def fetchparsednames(location, verbose=0):
    '''
    Return list of dicts parsing filenames
    '''
    return [dict(parsefilename(fn).items(), fileloc=os.path.join(location,fn))
                for fn in os.listdir(location)]
