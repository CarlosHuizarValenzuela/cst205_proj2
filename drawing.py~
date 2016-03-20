"""
This file is simply for your guys' convinience. This isn't part of our project but I'm hoping what I have done in this document can help you guys figure some stuff out.
driver.py is our project file
"""
import numpy as np
import cv2

img = cv2.imread("person.jpg")
img2 = cv2.imread("carnation.jpg")

"""
px = img[55, 55]
print(px)
#prints the color in that pixel [B, G, R]
#B = blue
#G = green
#R = red
#you can change the color of the pixel by typing:
img[55, 55] = [255, 255, 255]
It'll turn the pixel white.

#ROI is region of interest. It's kind of like a subimage in an image. It's where you want to work

img[100:150, 100:150] #this is your ROI
#You can set the ROI to a different color like this:
img[100:150, 100:150] = [255, 255, 255]

#Now we're going to grab a ROI and make it a variable
guy_face = img[37:111, 107:194]
#111-37 = 74 pixels is how many pixels there are going down (height) [think of arrays i.e. rows]
#194-107 = 87 pixels is how many pixels there are going to right (width) [in arrays, they're known as columns]
#74 x 87 or 87 x 74?
	#you start at coordinates: (107, 37) 
	#height: pixel #111
	#width: pixel #194

#Now we can redefine a new region of that image!
img[0:74, 0:87] = guy_face
#You just pasted guy_face on the upper left corner of your original image

Adding two images using openCV:
simpleAddPicture = img + img2
openCVAddPicture = cv2.add(img + img2)
addingWeightedPicture = cv2.addWeighted(img, 0.6, img2, 0.4, 0)
#0.6 means only use 60% of the image
#0.4 means only use 40% of the image
"""
#channels are the color values of Blue, Green, and Red
rows, cols, channels = img2.shape
roi = img[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#now apply a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
#cv2.THRESH_BINARY_INV the value for this either 0 or 1.
#if a pixel value is above 220, it'll be converted to 255. & if it's below 220, it'll be converted to black.
#then this will be flipped around because we are getting the inverse

mask_inv = cv2.bitwise_not(mask)
#not: means do not include the part that does not have mask [black area]
#mask_inv: inv means invisible part
#bitwise is a low-level logical operation [it's from C language] but it is more complicated.
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img[0:rows, 0:cols] = dst

cv2.imwrite('res.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()	
