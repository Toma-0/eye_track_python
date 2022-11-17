import cv2
import cv2
import time
import dec_eyeCv2

try:
    N = input()
    cap = cv2.VideoCapture("movie/"+N)
    start_time = time.time()
    frame_cnt = 0

  
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    video = cv2.VideoWriter(N+'_210_eye.mp4', fourcc, 20, (640, 360))
    
    
    while(True):
            #画面の読み込み
            ret, frame = cap.read()
           


            # 顔のランドマーク検出(2.の関数呼び出し)
            #dec_face.process(frame)
            dec_eyeCv2.process(frame)

            # 結果の表示
            #cv2.imshow('face', frame)
            
            video.write(frame)
            
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

except Exception as e:
    print(str(e))