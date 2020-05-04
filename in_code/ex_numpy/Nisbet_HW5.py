"""
Ian Nisbet
OCN 506
Homework 5
"""

# imports
import sys, os
import numpy as np
import pickle
import argparse

# create 2-D arrays 
aa = np.array(np.arange(12)).reshape((6,2))
bb = np.array(np.arange(12)).reshape((2,6))
cc = np.array(np.arange(12)).reshape((3,4))
dd = np.array(np.arange(12)).reshape((4,3))

print('\n2-D arrays of different shapes:')
print('\naa =')
print(aa)
print('\nbb =')
print(bb)
print('\ncc =')
print(cc)
print('\ndd =')
print(dd)

# indexing within the 2-D arrays

print('\nIndexing within the 2-D arrays')

print('\nfind the 3rd row, column 2 of aa')
print(aa[2:3, :1]) 

print('\nfind all rows, column 1 of bb')
print(bb[:, 0:1]) 

print('\nfind row 2, all columnts cc')
print(cc[1:2, :]) 

print('\nfind rows up to 3, column up to 3 of dd')
print(cc[:3, :3]) 


# Concatinating arrays

print('\nConcatenate aa to aa')
aa2 = np.concatenate((aa,aa), axis=1)
print(aa2)

# Copy arrays

print('\nCopy Arrays')
y = aa.copy()
print('\ny is a copy of aa')
print('\ny=')
print(y)

# fill arrays
print('\nFill Arrays with Scalar values')
print('\nFill y with all 1s')
y.fill(1)

print('\ny=')
print(y)

# find mean of arrays
print('\nfind mean of array rows')
m = np.mean(aa, axis=0)
print('\nm=')
print(m)

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make output directory if it does not exist
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

# save aa as a pickle
out_fn = out_dir + 'saved_array_aa.p'
pickle.dump(aa, open(out_fn, 'wb'))

# read the array back in
aa_loaded = pickle.load(open(out_fn, 'rb'))



def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()

parser.add_argument('-a', '--a_string', default='password', type=str)
parser.add_argument('-e', '--e_string', default='1234', type=str)
parser.add_argument('-b', '--integer_b', default=150, type=int)
parser.add_argument('-c', '--float_c', default=1.5, type=float)
parser.add_argument('-v', '--verbose', default=True, type=boolean_string)


# get the arguments
args = parser.parse_args()

# output
print('\nThe password is ' + args.a_string + args.e_string)

if args.verbose:
    print('\nThe average of b and c is:')
    
print((args.integer_b + args.float_c)/2)
