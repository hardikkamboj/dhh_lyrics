from video_lyrics_module import *

import cv2 

img = cv2.imread('krsna.png')

threshold_value = 0.85
bottom_value = int(img.shape[0]*threshold_value)
padding_value = 400

img2 = img[bottom_value:,padding_value:-padding_value]
print(get_text_from_image(img2))

cv2.imshow('image',img2)
cv2.waitKey(0)

print(img2.shape)

gray = get_grayscale(img2)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)


print(get_text_from_image(canny))
cv2.imshow('canny',canny)
cv2.waitKey(0)