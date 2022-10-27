#顔のランドマークを検出
import cv2
import setup_import
from imutils import face_utils
import dec_eye


def process(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = setup_import.face_detector(gray)

    face_mark = None

    for face in faces:
        face_mark = setup_import.shape_predictor(gray,face)
        face_mark = face_utils.shape_to_np(face_mark)
        
    if face_mark:
        dec_eye.detect_eye(face_mark,frame)
        #draw(face_mark,frame)

    return frame

"""
def draw(face_mark,frame):
    for (x,y) in face_mark:
        cv2.circle(frame,(x,y),1,(0, 255, 0), -1)
"""


def main(frame): 
    process(frame)