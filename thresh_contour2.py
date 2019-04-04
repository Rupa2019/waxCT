import cv2
import numpy as np
import matplotlib.pyplot as plt

def thresh_CT(imgray):
    test, thresh = cv2.threshold(imgray, 127, 255, 0)
    return thresh, test

def cont(imgray,thresh, ex=False):
     
    thresh[810:1020, 740:970] = [0]

    # Set all thresholds and countours
  
    if ex:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
    # Create Array of all the areas
    A = []
    for cnt in contours:
        A.append(cv2.contourArea(cnt))
  

    return [A, contours, hierarchy]

