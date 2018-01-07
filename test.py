# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:18:18 2017
@author: Rahul
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Coordinates(edges):
    wid_pix=list()
    leng_pix=list()
    for columns in range(edges.shape[1]):
        for rows in range(edges.shape[0]):
            if(edges[rows][columns]!=0):
                wid_pix.append(rows)
                leng_pix.append(columns)
                break
    return wid_pix






image=cv2.imread('znap24.jpg',cv2.IMREAD_COLOR)
#img2gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
red = image[400:600,500:1700,2]
red1=cv2.bilateralFilter(red,10,100,100)
ret,new=cv2.threshold(red,80,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

ret1,new1=cv2.threshold(red1,80,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('res1',new)
#cv2.imshow('res',new1)
'''kernel = np.ones((5,5),np.uint8)

ero = cv2.erode(new, kernel, iterations=1)
dil = cv2.dilate(ero, kernel,iterations=1)
dil = cv2.dilate(dil, kernel,iterations=1)
ero = cv2.erode(dil, kernel, iterations=1)
cv2.imshow('wq',ero)'''
edges=cv2.Canny(new1,100,200)
edges1=cv2.Canny(new,100,200)
wid_pixel=Coordinates(edges)
wid_pixel1=Coordinates(edges1)

cv2.imshow('edges',edges)     
viz=pd.Series(wid_pixel)
viz1=pd.Series(wid_pixel1)
plt.plot(viz)
plt.plot(viz1)
plt.show()
#length=leng_pix*sizeofeachpixel


cv2.waitKey(0)
cv2.destroyAllWindows()
