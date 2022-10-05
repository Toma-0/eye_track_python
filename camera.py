import cv2
import time
import face_landmark
import setup_import

try:
    #画面、開始時間、フレームの設定
    cap = setup_import.cap
    start_time = time.time()
    frame_cnt = 0

    while(True):
        #画面の読み込み
        ret, frame = cap.read()

        # 顔のランドマーク検出(2.の関数呼び出し)
        face_landmark.main(frame)

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

except Exception as e:
    print(str(e))