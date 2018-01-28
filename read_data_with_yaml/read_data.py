# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:08:02 2018

@author: bhavin.shah
"""

import yaml

def read_data():
    return yaml.load(open('335982.yaml', 'r'))

data = read_data()
print(data)
