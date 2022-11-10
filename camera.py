import cv2
import time
import dec_face
import setup_import
import dec_eyeCv2

try:
    #画面、開始時間、フレームの設定
    cap = setup_import.cap
    start_time = time.time()
    frame_cnt = 0

   
    fps_1 = int(cap.get(cv2.CAP_PROP_FPS))                    # カメラのFPSを取得
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    video = cv2.VideoWriter('video.mp4', fourcc, fps_1, (w, h))
    

    while(True):
        #画面の読み込み
        ret, frame = cap.read()
        imgBoxHsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        v = imgBoxHsv.T[2].flatten().mean()


        # 顔のランドマーク検出(2.の関数呼び出し)
        #dec_face.process(frame)
        dec_eyeCv2.process(frame,v)

        # 結果の表示
        cv2.imshow('face', frame)
        
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