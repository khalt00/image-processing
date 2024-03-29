#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:31:31 2022

@author: khale
"""


import os
import numpy as np
import shutil
import random


path_images = os.listdir('/home/khale/Documents/animals/images/train/')


# creating train / val /test 
new_root = '/home/khale/data/'

classes = []
for file in path_images:
    classes.append(file)


print(classes)
for obj in classes:
    os.makedirs(new_root+ 'train/' + obj)
    os.makedirs(new_root +'val/' + obj)
    os.makedirs(new_root + 'test/' + obj)
    
## creating partition of the data after shuffeling

for obj in classes:
    src = '/home/khale/Documents/animals/images/train/' + obj # folder to copy images from
    print(src)

    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)
    train_FileNames,val_FileNames,test_FileNames = np.split(np.array(allFileNames),[int(len(allFileNames)*0.75),int(len(allFileNames)*0.85)])

    ## here 0.75 = training ratio , (0.95-0.75) = validation ratio , (1-0.95) =  
    ##training ratio  

    # #Converting file names from array to list
    train_FileNames = [src+'/'+ name for name in train_FileNames]
    val_FileNames = [src+'/' + name for name in val_FileNames]
    test_FileNames = [src+'/' + name for name in test_FileNames]

    print('Total images  : '+ obj + ' ' +str(len(allFileNames)))
    print('Training : '+ obj + ' '+str(len(train_FileNames)))
    print('Validation : '+ obj + ' ' +str(len(val_FileNames)))
    print('Testing : '+ obj + ' '+str(len(test_FileNames)))
    
    ## Copy pasting images to target directory

    for name in train_FileNames:
        shutil.copy(name, new_root+'train/'+obj )
        

    for name in val_FileNames:
        shutil.copy(name, new_root+'val/'+obj )


    for name in test_FileNames:
        shutil.copy(name, new_root+'test/'+obj )
