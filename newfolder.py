#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:03:29 2022

@author: khale
"""

import os


path_image = os.listdir('/home/khale/Documents/animals/images/train/')

for file in path_image:
    os.makedirs(os.path.join('/home/khale/Documents/animals/labels/train/',file))

    
    
