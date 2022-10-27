from turtle import right
import cv2
import setup_import
from imutils import face_utils
import face_landmark

def detect_eye(facemark,frame):
    print("detect_eye")
    #距離が長くなる方を検出
    if facemark[37][1] > facemark[38][1]:
            top_right =facemark[37][1] 
    else :
        top_right =facemark[38][1] 

    if facemark[41][1] > facemark[40][1]:
        bottom_right =facemark[40][1] 
    else :
        bottom_right =facemark[41][1] 

    if facemark[43][1] > facemark[44][1]:
        top_left =facemark[43][1] 
    else :
        top_left =facemark[44][1] 

    if facemark[47][1] > facemark[46][1]:
        bottom_left =facemark[46][1] 
    else :
        bottom_left =facemark[47][1] 

    right_eye_coordinate = [top_right,bottom_right,facemark[36][0],facemark[39][0]]
    left_eye_coordinate = [top_left,bottom_left,facemark[42][0],facemark[45][0]]

    draw(right_eye_coordinate,left_eye_coordinate,frame)
    #img_keep(right_eye_coordinate,left_eye_coordinate,frame)
    

def draw(right_eye,left_eye,frame):   
    cv2.rectangle(frame, (right_eye[2], right_eye[1]), (right_eye[3], right_eye[0]), (0, 255, 0), thickness=1, lineType=cv2.LINE_4)
    cv2.rectangle(frame, (left_eye[2], right_eye[1]), (left_eye[3], left_eye[0]), (0, 255, 0), thickness=1, lineType=cv2.LINE_4)

def img_keep(right_eye,left_eye,frame):   
    right_eye_frame=frame[right_eye[2]:right_eye[1], right_eye[3]:right_eye[0]] 
    right_eye_frame=frame[left_eye[2]:left_eye[1], left_eye[3]:left_eye[0]]
