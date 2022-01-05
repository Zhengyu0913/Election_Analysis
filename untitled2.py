# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:15:12 2022

@author: fanzh
"""

import csv
import os


# Open the election results and read the file.
with open('election_results.csv') as election_data:

    # Print the file object.
     print(election_data)