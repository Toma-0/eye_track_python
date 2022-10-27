import cv2
from imutils import face_utils
import time
import dlib

def main():
    camera()

def setup_import():
    face_detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    

def camera():
        #画面、開始時間、フレームの設定
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        start_time = time.time()
        frame_cnt = 0

        while(True):
            #画面の読み込み
            ret, frame = cap.read()

            # 顔のランドマーク検出(2.の関数呼び出し)
            dec_face(frame)

            # 結果の表示
            cv2.imshow('face', frame)
            frame_cnt += 1

            # 'q'が入力されるまでループ
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # 後処理
        cap.release()
        cv2.destroyAllWindows()

        #終了時間と最終フレーム数からfpsを書き出し
        end_time = time.time()
        fps = frame_cnt / int(end_time - start_time)
        print("FPS=" + "{:.1f}".format(fps))

def dec_face(frame):
    face_cascade_path = '/usr/local/opt/opencv/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    src_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        face = frame[x:x+w, y:y+h]
        face_landmark(face)

def face_landmark(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = setup_import.face_detector(gray)

    face_mark = None

    for face in faces:
        face_mark = setup_import.shape_predictor(gray,face)
        face_mark = face_utils.shape_to_np(face_mark)

    dec_eye(face_mark,frame)

def dec_eye(facemark,frame):
    if facemark:
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

if __name__ == "__main__":
    main()

