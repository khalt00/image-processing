# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:19:55 2021

@author: Administrator
"""

import os

path_image = os.listdir('/home/khale/data/test/')

for file in path_image:
    path = f"/home/khale/data_label/train/{file}/"
    
    for i in range(1,21):
      file_name = str(i) + ".txt"
      i = i+1
      complete = os.path.join(path,file_name)
      file1 = open(complete, "w")
      file1.close()





	
