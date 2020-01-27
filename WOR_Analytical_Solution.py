# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:27:07 2020

@author: John.Whitehead
"""

import os, glob
import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', -1)

# Current Working Directory where RSM file lives
win_path = r'\\europe.shell.com\tcs\ams\pt.sgs\proj\south_america\br_development\dm\Spotfire_WRFM\DailySync'
# Change directory to location
os.chdir(win_path) # change working directory to win_path
# Read RSM dataframe
df = pd.read_csv(win_path + '\\' + 'RSM_no_header.csv',
                 delimiter='\t',
                 parse_dates=['DATE'],
                 dayfirst=True,
                 dtype={
                        'DailyChokePressWH_USC_PRESS': np.float64,
                        'DailyPressureWHP': np.float64,
                        'DailyPressureBHP': np.float64,
                        'DailyProdOil': np.float64, 
                        'DailyProdGas': np.float64,
                        'DailyProdWater': np.float64,
                        'DailyProdLiftGas': np.float64},
                error_bad_lines=False, low_memory=False).dropna(how='all')