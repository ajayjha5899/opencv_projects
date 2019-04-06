#Colours

import numpy as np
import cv2

def nothing(x) :
	pass

cap = cv2.VideoCapture(0)

while True :
	t = cv2.getTrackbarPos('Thresh val','Video')
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	image = frame

	blur1 = cv2.GaussianBlur(image,(3,3),0)
	morph_size = 2
	element = cv2.getStructuringElement(cv2.MORPH_RECT,(2*morph_size + 1, 2 * morph_size + 1), (morph_size,morph_size))
	cv2.morphologyEx(blur1,3,element)
	cv2.morphologyEx(blur1,2,element)
	blur2 = cv2.medianBlur(blur1,5)
	blur3 = cv2.bilateralFilter(blur2,9,75,75)

	cv2.imshow("blur3",blur3)

	hsv = cv2.cvtColor(blur3,cv2.COLOR_BGR2HSV)
	cv2.imshow("hsv",hsv)

	thresh = cv2.inRange(hsv,(0,26,69),(40,251,255))
	cv2.imshow("threshold",thresh)

	p = frame.shape

	cv2.line(frame,(p[1]/3,0),(p[1]/3,p[0]),(0,0,0),3)
	cv2.line(frame,(2*p[1]/3,0),(2*p[1]/3,p[0]),(0,0,0),3)
	cv2.line(frame,(p[1]/3,p[0]/2),(2*p[1]/3,p[0]/2),(0,0,0),3)

	max_area = 0
	
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for i in range(0,len(contours)) :
		cnt = contours[i]
		area = cv2.contourArea(cnt)
		if(area>max_area) :
			max_area = area
			j = i

	if max_area>0 :
		epsilon = 0.1 * cv2.arcLength(contours[j],True)
		approx = cv2.approxPolyDP(contours[j],epsilon,True)

		(x,y),radius = cv2.minEnclosingCircle(contours[j])

		x = int(x)
		y = int(y)
		radius = int(radius)

		cv2.circle(frame,(x,y),radius,(0,0,255),3)

		cx = x
		cy = y

		cv2.circle(frame,(cx,cy),10,(0,0,0),-1)

		font = cv2.FONT_HERSHEY_SIMPLEX

		if(cx<p[1]/3) :
			cv2.putText(frame,'Right',(cx,cy),font,1,(0,0,255),2)
		if(cx>2*p[1]/3) :
			cv2.putText(frame,'Left',(cx,cy),font,1,(0,0,255),2)
		if(cx>p[1]/3 and cx<2*p[1]/3 and cy<p[0]/2) :
			cv2.putText(frame,'Forward',(cx,cy),font,1,(0,0,255),2)
		if(cx>p[1]/3 and cx<2*p[1]/3 and cy>p[0]/2) :
			cv2.putText(frame,'Stop',(cx,cy),font,1,(0,0,255),2)
	
	cv2.imshow("Contoured",frame)

	if cv2.waitKey(1) & 0xFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()