import numpy as np
import cv2

frontFaceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
altFrontFaceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/newEye1.xml')
noseCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_nose.xml')
rightEarCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_rightear.xml') 
leftEarCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_leftear.xml')
mouthCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_mouth.xml')

img = cv2.imread('girl2.jpg', -1)
#_______________________________
# Load and configure dog nose
#_______________________________
#------------------------------------------------------!!!!!!!!!!!!!!!!!
#I SAID DOG NOSE, BUT I CHANGED MY TESTING IMAGE TO THE MUSTACHE IMAGE.
#SO, THROUGHOUT THE WHOLE DOCUMENT, THE THINGS RELATED TO img2 WILL BE REFFERED TO AS DOG_.... OR DOGWIDTH OR DOGHEIGHT, ETC.
#JUST PRETEND I SAID MUSTACHE
#I'M STILL FIXING SOME STUFF
#------------------------------------------------------!!!!!!!!!!!!!!!!!

img2 = cv2.imread('lip2.png', -1)

#img3 = cv2.imread('lip2.png', -1)
#create the mask for the mustache
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, dog_mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY_INV)
#ret, eye_mask = cv2.threshold(img3gray, 10, 255, cv2.THRESH_BINARY_INV)
#cv2.THRESH_BINARY_INV the value for this either 0 or 1.
#if a pixel value is above 250, it'll be converted to 255. & if it's below 250, it'll be converted to black.
#then this will be flipped around because we are getting the inverse
dog_mask_inv = cv2.bitwise_not(dog_mask)
#eye_mask_inv = cv2.bitwise_not(eye_mask)
# Convert glasses image to BGR
# and save the original image size (used later when re-sizing the image)
img2 = img2[:,:,0:3]
#img3 = img3[:,:,0:3]
originalDogHeight, originalDogWidth = img2.shape[:2]
print(originalDogHeight)
print(originalDogWidth)
#originalEyeHeight, originalEyeWidth = img3.shape[:2]
#print(originalEyeHeight)
#print(originalEyeWidth)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imwrite('grayversion.jpg', gray)
faces = frontFaceCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize =(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
#(x, y)
#w stands for width
#h stands for height
for(x, y, w, h) in faces:

	#cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
	
	#roi stands for region of interest. It's where you want to work on.
	
	#the gray-scale of the original image:
	roi_gray = gray[y:y+h, x:x+w]
	#the colored version of the original image:
	roi_color = img[y:y+h, x:x+w]
	#the region of interest for the mouth (it's colored):
	roi_grayMouthArea = gray[y+250:y+h, x:x+w]
	roi_colorMouthArea = img[y+250:y+h, x:x+w]
	
	eyesPair = eyeCascade.detectMultiScale(roi_gray) #returns cordinates, width, and height at where you want to work with
	nose = noseCascade.detectMultiScale(roi_gray)
	mouth = mouthCascade.detectMultiScale(roi_grayMouthArea)
	
	for(x2, y2, w2, h2) in eyesPair:
		#below is where CARLOS is supposed to work:
		
		break
		
	for(x4, y4, w4, h4) in mouth:
		#cv2.rectangle(roi_color, (x4, y4), (x4+w4, y4+h4), (0, 0, 225), 2)
		#below is where NICOLAS is supposed to work:
		#except you need to keep changing your cascade until you find a more accurate one.
		
		break

	for(x2, y2, w2, h2) in nose: 
		#cv2.rectangle(roi_color, (x2, y2), (x2+w2, y2+h2), (0, 225, 0), 2)
		y2 = y2+20
		x2 = x2+5
		#The dog image should be 3 times the width of the nose
		dogWidth = 2*w2
		dogHeight = dogWidth * originalDogHeight / originalDogWidth
		print(dogWidth)
		print(dogHeight)
		#center the dog nose on the bottom of the nose
		xn1 = x2 -(dogWidth/4)
		xn2 = x2 + w2 + (dogWidth/4)
		yn1 = y2 + h2 - (dogHeight/2)
		yn2 = y2 + h2 + (dogHeight/2)
		
		if xn1 < 0:
			xn1 = 0
		if yn1 < 0:
			yn1 = 0
		if xn2 > 640:
			xn2 = w2
		if y2 > 320:
			yn2 = h2
		
		#Re-canculate the width and height of the dog's nose image
		dogWidth = xn2 - xn1
		dogHeight = yn2 - yn1
		
		#Re-size the original image and the masks to the dog's nose's original sizes
		#calculated above
		dogNose = cv2.resize(img2, (dogWidth, dogHeight), interpolation = cv2.INTER_AREA)
		mask = cv2.resize(dog_mask, (dogWidth, dogHeight), interpolation = cv2.INTER_AREA)
		mask_inv = cv2.resize(dog_mask_inv, (dogWidth, dogHeight), interpolation = cv2.INTER_AREA)
		print(mask.size)
		
		#take ROI for dog nose from background equal to size of ROI of dog nose image
		roi_nose = roi_color[yn1:yn2, xn1:xn2]
		print(roi_nose.size)
		
		#roi_bg contains the original image only where the dog nose is not in the region that is the size of the dog nose
		roi_bg = cv2.bitwise_and(roi_nose, roi_nose, mask = mask_inv)
		cv2.imwrite('roiBG.png', roi_bg)
		#roi_fg contains the image of the dog nose only where the dog nose is
		roi_fg = cv2.bitwise_and(dogNose, dogNose, mask=mask)
		cv2.imwrite('roiFG.png', roi_fg)
		#join the roi_bg and roi_fg
		dst = cv2.add(roi_bg, roi_fg)
		roi_color[yn1:yn2, xn1:xn2] = dst
		
		break
cv2.imwrite('newImg.png', img)
