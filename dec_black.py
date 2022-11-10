import cv2
import numpy as np

def main():
    frame =cv2.imread("temple.PNG")
    #cv2.imwrite("/Users/toma/Desktop/git/jikken_eye_python/tmp.PNG",frame)
    dec_color(frame)
    #template(frame)
    #circle(frame)


def dec_color(frame):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    
    lower_color = np.array([0, 0, 5])
    up_color= np.array([155, 255, 255])
    
    
    frame_mask = cv2.inRange(hsv,lower_color,up_color)

    contours, _ = cv2.findContours(frame_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
   
    for i in range(0, len(contours)):
        if len(contours[i]) > 0:
            # remove small objects
            if cv2.contourArea(contours[i]) < 500:
                 continue

            cv2.polylines(frame, contours[i], True, (255, 255, 255), 1)
            cv2.imwrite("/Users/toma/Desktop/git/jikken_eye_python/photo.jpeg",frame)

def template(frame):
    temp = cv2.imread("temple.PNG")

    result = cv2.matchTemplate(frame, temp, cv2.TM_CCOEFF_NORMED)
    ys, xs = np.where(result >= 0.9)

# 描画する。
    for x, y in zip(xs, ys):
        cv2.rectangle(
            frame,
            (x, y),
            (x + temp.shape[1], y + temp.shape[0]),
            color=(0, 255, 0),
            thickness=2,
        )
        cv2.imwrite("/Users/toma/Desktop/git/jikken_eye_python/photo.PNG",frame)

def circle(frame):
    frame = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,param1=500, param2=55, minRadius=100, maxRadius=0)
    

    for cx, cy, r in circles.squeeze(axis=0).astype(int):
       # 円の円周を描画
        cv2.circle(frame, (cx, cy), r, (0, 255, 0), 6)
        # 円の中心を描画
        cv2.circle(frame, (cx, cy), 2, (0, 255, 0), 4)
        cv2.imwrite("/Users/toma/Desktop/git/jikken_eye_python/photo.PNG",frame)
   
if __name__ == "__main__":
       main()




