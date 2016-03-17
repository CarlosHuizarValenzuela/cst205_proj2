import numpy as np
import cv2

frontFaceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
altFrontFaceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/newEye1.xml')
noseCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_nose.xml')
rightEarCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_rightear.xml') 
leftEarCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_leftear.xml')
mouthCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_maouth.xml')

img = cv2.imread('angelina.jpg')
img2 = cv2.imread('dog.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayversion.jpg', gray)
faces = frontFaceCascade.detectMultiScale(gray, 1.3, 5)
#(x, y)
#w stands for width
#h stands for height
for(x, y, w, h) in faces:

	cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
	
	#roi stands for region of interest. It's where you want to work on.
	
	#the gray-scale of the original image:
	roi_gray = gray[y:y+h, x:x+w]
	#the colored version of the original image:
	roi_color = img[y:y+h, x:x+w]
	#the region of interest for the mouth (it's colored):
	roi_grayMouthArea = gray[y+250:y+h, x:x+w]
	roi_colorMouthArea = img[y+250:y+h, x:x+w]
	
	cv2.imwrite('mainPart.png', roi_gray)
	cv2.imwrite('part.png', roi_colorMouthArea)
	
	eyesPair = eyeCascade.detectMultiScale(roi_gray) #returns cordinates, width, and height at where you want to work with
	nose = noseCascade.detectMultiScale(roi_gray)
	mouth = mouthCascade.detectMultiScale(roi_grayMouthArea)
	
	
	for(x3, y3, w3, h3) in eyesPair:
		cv2.rectangle(roi_color, (x3, y3), (x3+w3, y3+h3), (225, 0, 0), 2)
		#below is where CARLOS is supposed to work:
		
	for(x4, y4, w4, h4) in mouth:
		cv2.rectangle(roi_color, (x4, y4), (x4+w4, y4+h4), (0, 0, 225), 2)
		#below is where NICOLAS is supposed to work:
		#except you need to keep changing your cascade until you find a more accurate one.
		
	for(x2, y2, w2, h2) in nose: 
		cv2.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (0, 225, 0), 2)
		
		rows,cols = img2.shape[:2]
		roi = img[y2:y2+159, x2:x2+159]
		img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
		
		"""#img2 = cv2.resize
		ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)
		mask_inv = cv2.bitwise_not(mask)
		#not: means do not include the part that does not have mask [black area]
		#mask_inv: inv means invisible part
		#bitwise is a low-level logical operation [it's from C language] but it is more complicated.
		# Now black-out the area of logo in ROI
		img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

		# Take only region of logo from logo image.
		img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

		# Put logo in ROI and modify the main image
		dst = cv2.add(img1_bg,img2_fg)
		"""
cv2.imwrite('newImg.png', img)
