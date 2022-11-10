import cv2
import dec_black

def process(face):
    eye_cascade_path = '/usr/local/opt/opencv/share/opencv4/haarcascades/haarcascade_eye.xml'

    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
    src_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(src_gray,scaleFactor=4.3,minNeighbors=7)
    
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        eye = face[ey:ey+eh,ex:ex+ew]
        dec_black.dec_color(eye)
        #dec_black.circle(eye)
        #dec_black.template(eye)
        #cv2.imshow("eye",eye)
        