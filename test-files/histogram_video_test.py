# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import cv2 as cv
import numpy as np

# load the input image and convert it to 

#image = cv.imread("DSC07579.jpg")
cap = cv.VideoCapture(1)
while(1):
    
    ret, frame = cap.read()

    image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    histSize = 256
    histRange = (0, 256) # the upper boundary is exclusive
    accumulate = False
    hist = cv.calcHist([image], [0], None, [256], [0, 256])
    #hist = cv.calcHist([image], [0], None, [histSize], histRange, accumulate=accumulate)
    hist_w = 512
    hist_h = 400
    bin_w = int(round( hist_w/histSize ))
    
    histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
    # compute a grayscale histogram
   
    cv.normalize(hist, hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

    
    for i in range(1, histSize):
        cv.line(histImage, ( bin_w*(i-1), hist_h - int(hist[i-1]) ), ( bin_w*(i), hist_h - int(hist[i]) ), ( 255, 255, 255), thickness=2)


    cv.imshow('Source image', frame)

    cv.namedWindow('calcHist Demo', cv.WINDOW_NORMAL) 
    cv.resizeWindow('calcHist Demo', 960, 540)
    cv.imshow('calcHist Demo', histImage)

    # Exit when the 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
         break

    # Release the video capture object and close all windows
cap.release()
cv.destroyAllWindows()
