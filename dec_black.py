import cv2
import numpy as np

def dec_color(frame,hsv,v):
    num = v/4
    lower_color = np.array([0, 0, 0])
    up_color= np.array([255, 255, int(num)])
    
    
    frame_mask = cv2.inRange(hsv,lower_color,up_color)


    contours, _ = cv2.findContours(frame_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
   
    for i in range(0, len(contours)):
        if len(contours[i]) > 0:
            # remove small objects
            if cv2.contourArea(contours[i]) < 500:
                 continue

            cv2.polylines(frame, contours[i], True, (255, 255, 255), 1)
            
def black(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
    

        for circle in circles[0,:]:
            cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 165, 255), 2)
            cv2.circle(frame, (circle[0], circle[1]), 2, (0, 0, 255), 3)
            
