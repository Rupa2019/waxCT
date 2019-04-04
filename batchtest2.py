import cv2
import os
print (os.environ['CONDA_DEFAULT_ENV'])
import numpy as np
import matplotlib.pyplot as plt
from thresh_contour import *
from detect_void import *
from detect_CB import *
from WaxTurbine2 import *
import glob
import os
import progressbar
import csv
import traceback

# Void 2
#directory = '/media/iain/My Book Duo/Wax CT Project/CT Images/3DCT/BA0502315 [2018-02-09 00.14.43]/Results'
# Core break 2
 ## commented out by Rupa:
#directory = '/media/rupa/40E80E69E80E5E12/Wax_CT_Project/CT_Images/3DCT/BA0502617 [2018-02-11 04.53.03]/Results'
# Core break 2
## commented out by Rupa:
# directory = '/media/iain/My Book Duo/Wax CT Project/CT Images/3DCT/BA0502585 [2018-02-10 03.26.56]/Results'
# Core break 3
# directory = '/media/iain/My Book Duo/Wax CT Project/CT Images/3DCT/BA0502651 [2018-02-12 13.09.10]/Results'



class Anomaly():
    def __init__(self, filename):
        self.filename = filename
        self.contDict = self.getContours(ex=True)
        self.ex_contDict = self.getContours(ex=False)
        self.VOIDS = self.getAnomaly(self.contDict, isVoids=True)
        self.CB = self.getAnomaly(self.ex_contDict, isVoids=False)
        self.result = self.getResult()

    def getContours(self,  ex):
        contDict = ScanCT(self.filename, ex)
        return contDict

    def getAnomaly(self, contDict, isVoids):
        if contDict['contours']:
            if isVoids:
                anomaly = detect_void(self.contDict['contours'], contDict['hierarchy'])
            else:
                anomaly = detect_CB(self.ex_contDict['contours'],0.05)
        else:
            anomaly = []
        return anomaly
    
    def getResult(self):
        if len(self.VOIDS) + len(self.CB)/2 ==0:
            result = 0
        # or len(CB) >=6 
        else: 
            result = 1
        return result                      
        
def main():
    directory = '/media/rupa/40E80E69E80E5E12/Wax_CT_Project/CT_Images/3DCT/BA0502257 [2018-02-08 19.58.23]/Results'
    #resultsFile = '/home/rupa/projects/defectDetection/results/resultsFileIndDefSliceNo.csv'
    resultC = 0
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".tif"):
            print(filename)
            absFilename = os.path.join(directory, filename)
            dect = Anomaly(absFilename)
            if dect.result:
                resultC =resultC+1
                voids = dect.VOIDS
                cb = dect.CB
                sliceNo = resultC
                fileName = dect.filename
                im = dect.contDict['im']
                contours = dect.contDict['contours']
            else:
                if resultC >= 50:
                    cv2.drawContours(im, contours, -1, (0,255,0), 1)
                    cv2.drawContours(im, cb, -1, (0,0,255), 1)
                    cv2.drawContours(im, voids, -1, (0,0,255), 1)
                    cv2.namedWindow( 'image',cv2.WINDOW_NORMAL)
                    cv2.imshow('image', im)
                    cv2.imwrite('test2.jpg',im)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    print()
                    print(len(voids), "void(s) present")
                    print(len(cb), "CB(s) present")
                    print(fileName)
                    print(sliceNo)
                    resultC=0

                    

if __name__ == "__main__":
    main()

