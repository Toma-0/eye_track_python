import dlib
import cv2


face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

 # Camera
cap = cv2.VideoCapture(0)
w=cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
h=cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)