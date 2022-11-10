import dlib
import cv2


face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

 # Camera
cap = cv2.VideoCapture(0)
w_tmp=1280
h_tmp=1080
w=cap.set(cv2.CAP_PROP_FRAME_WIDTH, w_tmp)
h=cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h_tmp)