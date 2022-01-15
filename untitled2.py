# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:15:12 2022

@author: fanzh
"""

import csv
import os


# Open the election results and read the file.
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)