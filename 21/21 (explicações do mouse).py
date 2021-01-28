import cv2
import numpy as np
from numba import njit



def mouse_event(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:  #EVENT_LBUTTONDOWN significa que vai ser com um click. Existe o double click em outro.
        print (x,y) 
cv2.namedWindow("frame") #abre uma tela
cv2.setMouseCallback("frame",mouse_event) #são os clicks
      
   
    #cv2.imshow()
   # cv2.waitKey(0)

