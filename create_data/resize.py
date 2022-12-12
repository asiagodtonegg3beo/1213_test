# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 03:16:28 2022

@author: suckmydick
"""
import os
import cv2


for i in range(6,9,1):
    print(i)
    path = 'hard_example_0.' + str(i) + '/'
    
    img_path = os.listdir(path)
    
    for i in img_path:
        save_path = os.path.join(path,i)
        img = cv2.imread(os.path.join(path,i))
        img = cv2.resize(img, (64,64), interpolation=cv2.INTER_AREA)
        cv2.imwrite(save_path, img)
        print(i)

