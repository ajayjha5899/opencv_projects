import cv2
import numpy as np

def drawBoundary(a00, a01, a10, a11) :
	global height
	points = np.array([[a00, 0], [a01, 0], [a10, height], [a11, height]], np.int32)
	cv2.polylines(frame, [points], True, (0,255,0),3)


face_cascade = cv2.CascadeClassifier('C:/Users/lenovo/Desktop/Internship/Fusion Informatcs/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
#**select resolution of video capture**#
width = 1000												#<----------INPUT--------
height = 800												#<----------INPUT--------
cap.set(3,width)
cap.set(4,height)
cv2.namedWindow("FaceDetector",cv2.WINDOW_AUTOSIZE)
#**select points of polygon starting from x00 taken in clockwise fashion**#
x00 = 250												#<----------INPUT--------
x01 = width - 250										#<----------INPUT--------
x10 = width - 400										#<----------INPUT--------
x11 = 400												#<----------INPUT--------
 
while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#drawing roi boundary shape
	drawBoundary(x00, x01, x10, x11)
	
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces :
		l1 = (-height/x11-x00)*(x-x00)
		l2 = (-height/x10-x01)*(x+w-x01)
		condition = (y >= l1) and (y+h <= l2) and (y <= l2) and (y+h >= l1)
		print(condition)
		if(condition) :
			
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)

	#**press 'q' to exit the  program**#
	cv2.imshow("FaceDetector",frame)
	if cv2.waitKey(25) & 0xFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()