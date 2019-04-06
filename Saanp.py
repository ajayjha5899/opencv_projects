print ("Press ESC to quit")
print (" W for up \n A for left \n S for down \n D for right")

import cv2
import numpy as np
import random

cv2.namedWindow("Saanp_v1.0 by chaupatt",cv2.WINDOW_NORMAL)
main = np.zeros((600,600,3),np.uint8)
cv2.rectangle(main,(0,0),(610,610),(0,0,255),20)
#grid
t = 600
while (t) :
	cv2.line(main,(0,t),(600,t),(45,38,0),1)
	cv2.line(main,(t,0),(t,600),(45,38,0),1)

	t -= 30

snake = [[315,315],[315,345],[315,360],[315,375]]

def newfood() :
	cv2.circle(main,(int((random.randint(0,600)/30)+15),int((random.randint(0,600)/30)+15)),7,(0,255,0),-1)

def moveup() :
	global snake
	while True :
		for i in snake :
			cv2.circle(main,tuple(i),8,(0,255,255),3)
			i[1] -= 30 
			#if i[0] < 0 or i[1] < 0 :
			#	break

while True :
	cv2.imshow("Saanp_v1.0 by chaupatt",main)
	newfood()
	moveup()

	if cv2.waitKey(200) == ord('n') :
		pass
	elif cv2.waitKey(200) == 27 :
		break

cv2.destroyAllWindows()