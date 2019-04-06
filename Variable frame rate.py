print ("chaupatt_pro")

import cv2

def nothing(x) :
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
cv2.createTrackbar("Frame rate","Video",1,60,nothing)
font = cv2.FONT_HERSHEY_SIMPLEX

while True :
    ret, frame = cap.read()
    k = cv2.getTrackbarPos("Frame rate","Video")
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.putText(gray,str(k),(2,25),font,1,(255,255,255),2)
    cv2.imshow("Video",gray)

    if cv2.waitKey(int(1000/(k))) == 27 :
        break
cv2.destroyAllWindows()
