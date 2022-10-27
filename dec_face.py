import cv2
import face_landmark
import dec_eyeCv2

def process(frame):
    face_cascade_path = '/usr/local/opt/opencv/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    src_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(src_gray)
    

    for x, y, w, h in faces:
        face = frame[y:y+h,x:x+w]
        #face_landmark.main(face)
        dec_eyeCv2.process(face)
        

