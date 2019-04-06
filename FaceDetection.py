import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('C:/Users/lenovo/Desktop/Internship/Fusion Informatcs/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
#**select resolution of video capture**#
width = 600					#<----------INPUT--------
height = 400 				#<----------INPUT--------
cap.set(3,width)
cap.set(4,height)
cv2.namedWindow("FaceDetector",cv2.WINDOW_AUTOSIZE)

#**select roi size of square (select dimension of square)**#
size = 250					#<----------INPUT--------

center_x = width/2
center_y = height/2
roi_x1 = int(center_x - size/2)
roi_x2 = int(center_x + size/2)
roi_y1 = int(center_y - size/2)
roi_y2 = int(center_y + size/2)
 
while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#drawing roi boundary rectangle
	cv2.rectangle(frame,(roi_x1, roi_y1),(roi_x2, roi_y2),(255,0,0),2)

	faces = face_cascade.detectMultiScale(gray, 1.5, 5)
	for (x,y,w,h) in faces :
		condition = (roi_x1 < x) and (roi_x2 > x+w) and (roi_y1 < y) and (roi_y2 > y+h)
		print(condition)
		if(condition) :
			
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)

	#**press 'q' to exit the  program**#
	cv2.imshow("FaceDetector",frame)
	if cv2.waitKey(25) & 0xFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()