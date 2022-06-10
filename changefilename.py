	# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os


path_image = os.listdir('/home/khale/Documents/animals/images/train/')

for file in path_image:

    path = os.chdir(f"/home/khale/data/val/{file}/") #Here put the path of your folder where your images are stored
    
    image_name = input("Enter your Image name: ") #Here, enter the name you want your images to have
    
    i = 1
    print(file)
    for file in os.listdir(path):
    
        new_file_name = image_name+ str(i) + ".jpg" #here you can change the extention of your renmamed file.
        os.rename(file,new_file_name)
    
        i+=1
    
    input("Renamed all Images!!")
