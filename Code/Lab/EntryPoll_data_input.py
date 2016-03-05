"""
Data Bootcamp entry poll

Prepared for Data Bootcamp course at NYU
* http://databootcamp.nyuecon.com/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Lab

Written by Dave Backus, February 2016
Created with Python 3.5
"""
"""
import packages, check versions
"""
import sys
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

print('\nPython version: ', sys.version)
print('Pandas version: ', pd.__version__, '\n')

"""
read data from internet source
"""
url1 = 'http://pages.stern.nyu.edu/~dbackus/Data/'
url2 = 'Data-Bootcamp-entry-poll_s16.csv'
url = url1 + url2
file = url2

variables = ['time', 'program', 'career', 'code_exp', 'stats_exp', 'media',
             'other', 'major', 'data', 'why', 'topics']
ep = pd.read_csv(url, header=0, names=variables)
print('Dimensions:', ep.shape)
print('\nData types:\n', ep.dtypes, sep='')

#%%
# summarize results
for var in list(ep)[1:9]:
    print('\n')
    print(var, '\n', ep[var].value_counts(), sep='')

#%%
ep['media'] = ep['media'].str.split(',')
