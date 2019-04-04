import cv2
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def detect_CB(contours_ex,TOL):

    # This method compares the shape of each contour to every other one.
    # If there are no matching shapes then it is taken as core break
    # This method ignores any voids by taking external contours only

    ret =[]
    CB=[]
    MT = []

    for cnt1 in contours_ex:
        for cnt2 in contours_ex:ret.append(cv2.matchShapes(cnt1,cnt2,3,0.0))
        ret = np.hstack(ret)    
       
       
        if np.size((np.where(ret<=TOL))) <= 2: CB.append(cnt1)
            
        ret =[]
  
    # Returns the countours of any core breaks
    return CB


def detect_CB_area(A_ex):
    # Area method: does not work when core breaks into similar size shapes
    # do not use
    CB =[]
    TOL = 50
    # 
    for i in A_ex: CB.append(np.size(np.where(np.logical_and(A_ex>=i-TOL, A_ex<=i+TOL))))

    # If standard dev is great than 0 then there is a either a core break or something wrong
    return np.std(CB)
