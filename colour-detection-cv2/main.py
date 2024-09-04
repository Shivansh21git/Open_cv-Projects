import cv2
import numpy as np
from PIL import Image

colour = [0,255,255]  #------> BGR format
def con(frame):
    contours, _ = cv2.findContours(colmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        maxcon = max(contours,key =cv2.contourArea) 
        max_area = cv2.contourArea(maxcon)
        # print(max_area)         
        if max_area >= 1000:    # we are filtring out small detected areas in frame 
         return maxcon          # passsing max contour detected 

def climt(cbgr):                # colour value & limit defining function 
    c= np.uint8([[cbgr]])
    hsvc = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lLimit= hsvc[0][0][0]-10,200,100
    uLimit = hsvc[0][0][0]+20,255,255

    lLimit = np.array(lLimit, dtype=np.uint8)
    uLimit = np.array(uLimit, dtype=np.uint8)

    return lLimit,uLimit

# capturing video frame 
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
while(cap.isOpened()):
    ret, frame = cap.read()
    gblur = cv2.GaussianBlur(frame,(5,5),0)             # adding gausian blur to remove noise from frame
    hsvimg = cv2.cvtColor(gblur, cv2.COLOR_BGR2HSV)     # converting BGR ---> HSV 
    lLimit,uLimit = climt(colour)                       # getting limits
    
    # for manual range setting --------->
    # print(f'lower{lLimit}')
    # print(f'upper{uLimit}')
    # lLimit = np.array([43,106,170])
    # uLimit = np.array([179,220,255])

    colmask = cv2.inRange(hsvimg,lLimit,uLimit)        # filtring out colour range other than boundations
    maxconv = con(colmask)                             # getting maximum contour area 
    # print(maxconv)
    # wcolmask = cv2.bitwise_and(frame,frame,mask=colmask)   #---------------> this shows the frame with only detected object with its colour                 #---------------> this shows the frame with only detected object with white colour

    # msk = np.zeros_like(frame)
    if maxconv is not None:
        # cv2.drawContours(frame,[maxconv],-1,(0,255,255),-1)
        # frame = cv2.bitwise_and(frame,colmask)
        
        x, y, w, h = cv2.boundingRect(maxconv)
    # Draw the bounding box on the image
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if ret:

        # Display the resulting frame
        cv2.imshow('Frame',frame)
        # Press esc to exit
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()