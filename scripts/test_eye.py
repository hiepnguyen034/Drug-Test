import cv2 
import numpy as np 
import scipy.misc


image = cv2.imread('hiep.png')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye = eye_cascade.detectMultiScale(image)

#left
left_eye = image[eye[0][1] : eye[0][1]+ eye[0][3] , eye[0][0] : eye[0][0]+eye[0][2]]
# cv2.imshow('eye', left_eye)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('left.jpg', left_eye)

#right
right_eye = image[eye[2][1] : eye[2][1]+ eye[2][3] , eye[2][0] : eye[2][0]+eye[2][2]]
# cv2.imshow('eye', right_eye)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('right.jpg', right_eye)
