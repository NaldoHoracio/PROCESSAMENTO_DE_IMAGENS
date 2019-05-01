# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:15:48 2019

@author: horacio
"""

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2 as cv
import glob as glb
import math
import os

folders = glb.glob('/home/horacio/Imagens/TESTE')
image_names_list = []
for folder in folders:
    for f in glb.glob(folder + '/*.png'):
        image_names_list.append(f)

read_images = []        

for image in image_names_list:
    #read_images.append(cv.imread(image, cv.IMREAD_GRAYSCALE))
    read_images.append(cv.imread(image, cv.IMREAD_COLOR))

print(read_images)