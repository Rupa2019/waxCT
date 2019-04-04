import cv2
import numpy as np
import matplotlib.pyplot as plt
from thresh_contour2 import *
from detect_void import *
from detect_CB import *

def ScanCT(filename, ex):

    # ----------------------------------------------------------------------------------------

    # Read in image
    im = cv2.imread(filename)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    #------------------THRESHOLDING AND CONTOURING--------------------------------------------

    # Set threshold

    _, thresh = cv2.threshold(imgray, 127, 255, 0)

    # Set contours, internal and external
    A, contours, hierarchy = cont(imgray,thresh, ex)
  

    #   A    = array of all contour areas
    #   A_ex = array of all external contour areas
    contDict = {'im':im, 'imgray':imgray, 'A': A, 'contours':contours, 'hierarchy':hierarchy}
    
    return contDict
    # Check if contours exist, if not --> end.

    ''''
    if contours == []: 
        result = 0
        CB = 0
        VOIDS =  0


        return (result, im, contours, CB, VOIDS)

    # -------------------VOID DETECTION--------------------------------------------------------

    VOIDS = detect_void(contours, hierarchy)

    # ----------------CORE BREAK DETECTION-----------------------------------------------------

    # Look for core breaks in external contours, second term is the match tolerance

    CB = detect_CB(contours_ex,0.05)

    # ---------------------RESULTS-------------------------------------------------------------

    if len(VOIDS) + len(CB)/2 ==0 :result = 0
        # or len(CB) >=6 
    else: 
        result = 1


    return (result, im, contours, CB, VOIDS)
    '''