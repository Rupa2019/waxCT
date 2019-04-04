import cv2
import numpy as np
import matplotlib.pyplot as plt


def detect_void(contours, hierarchy):

    # Find inner countours
    VOIDS = [contours[i] for i in range(len(contours)) if hierarchy[0][i][3] >= 0] # Could build a minimum area size of void here
    
    return VOIDS

