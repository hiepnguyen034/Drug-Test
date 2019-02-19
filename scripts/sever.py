from flask import Flask, request, Response, render_template, redirect, url_for
import time
import requests
import label_image
import os
import cv2 
import pickle as pkl

PATH_TO_TEST_IMAGES_DIR = 'C:/Users/Hiep Nguyen/drug_test/scripts/images'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('getImage.html')

# save the image as a picture
@app.route('/image', methods=['POST', 'GET'])
def image():
	if request.method == 'POST':
		i = request.files['image']  # get the image
		f = 'picture.jpg'
		i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
		image = cv2.imread('C:/Users/Hiep Nguyen/drug_test/scripts/images/picture.jpg')

		eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
		eye = eye_cascade.detectMultiScale(image)

		left_eye = image[eye[0][1] : eye[0][1]+ eye[0][3] , eye[0][0] : eye[0][0]+eye[0][2]]
		#cv2.imshow('eye', left_eye)

		cv2.imwrite('picture.jpg', left_eye)
		label = label_image.predict('C:/Users/Hiep Nguyen/drug_test/scripts/images/picture.jpg')
		advice = 'something'

		if label == 'normal':
			with open('C:/Users/Hiep Nguyen/drug_test/scripts/normal.txt', 'r') as ad:
				advice = ad.read()
		else:
			with open('C:/Users/Hiep Nguyen/drug_test/scripts/drugs.txt', 'r') as ad:
				advice = ad.read()
 
		with open('result.txt', 'w') as out:
			out.write(advice)
		return ""


	else:
		while(not os.path.isfile('result.txt')):
			pass
		else:
			with open('result.txt', 'r') as infile:
				output = infile.read()
				infile.close()
				os.remove('result.txt')
				return render_template('resultTemplate.html', result = output)
 

if __name__ == '__main__':
    app.run(debug=True)