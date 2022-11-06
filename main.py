from operator import contains
import os
import urllib.request as req
from xmlrpc.client import boolean
from zlib import MAX_WBITS

from sqlalchemy import true
from app import app
from flask import Flask, request, redirect, jsonify, send_file
from werkzeug.utils import secure_filename
from PIL import Image, ImageOps
from ImageTransformations import ImageTransformationsDecider
import io



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])
ALLOWED_TRANSFORMATIONS = set(['anticlockwise','clockwise','flipvertical','fliphorizontal','rotate','thumbnail','grayscale','resize'])
MANDATORY_KEY=set(['transformations'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/transformationslist', methods=['GET'])
def getTransformationslist():
	resp = jsonify({'message' : 'success', 'code':200, "transformations":['anticlockwise','clockwise','flipvertical','fliphorizontal','rotateDegrees_90','grayscale','resizeWidthHeight_100_50','thumbnail']})
	return resp

@app.route('/transformations', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']

	#check if file is uploaded
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp

	#retrieve file for further processing	
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		fileExtension = filename.split(".")[-1]
		if fileExtension == "jpg":
			fileExtension = 'png'
		
		#open image and get height and width
		img = Image.open(file.stream)
		#MaxHEight, MaxWidth = img.size
		#resizeHeight = MaxHEight
		#resizeWidth = MaxWidth
		#rotationDegree = 0
		#print(MaxHEight,MaxWidth)
		tempVal = 0
		
		#Check if keys contain transformations
		if (request.form.keys() >= {"transformations"}):
			tempVal = 1
			
		if(tempVal == 0):
			resp = jsonify({'message' : 'please enter required transformations.'})
			resp.status_code = 400
			return resp
		
	
		#retrieve key values
		for key in request.form:
			print(key,request.form[key])

			if key == "transformations":
				if(request.form[key] != ''):
					transformationsValue = request.form[key]
				else:
					resp = jsonify({'message' : 'please enter valid transformation(s).'})
					return resp
		
			# if key == "height":
			# 	if((request.form[key]).isdigit()):
			# 		resizeHeight = int(request.form[key])
			# 		if(round(resizeHeight)> MaxHEight):
			# 			resp = jsonify({'message' : 'resize height is greater than image height'})
			# 			resp.status_code = 400
			# 			return resp
			# 	else:
			# 		resp = jsonify({'message' : 'resize height is not a valid number'})
			# 		resp.status_code = 400
			# 		return resp

			# if key == "width":
			# 	if((request.form[key]).isdigit()):
			# 		resizeWidth = int(request.form[key])
			# 		if(round(resizeWidth)> MaxWidth):
			# 			resp = jsonify({'message' : 'resize width is greater than image width'})
			# 			resp.status_code = 400
			# 			return resp
			# 	else:
			# 		resp = jsonify({'message' : 'resize width is not a valid number'})
			# 		resp.status_code = 400
			# 		return resp

			# if key == "degree":
			# 	if((request.form[key]).isdigit()):
			# 		rotationDegree = int(request.form[key])
			# 		print (rotationDegree)
			# 		if(rotationDegree != 90 and rotationDegree != 180 and rotationDegree != 270):
			# 			resp = jsonify({'message' : 'enter a valid rotation degree : 90, 180, 270'})
			# 			resp.status_code = 400
			# 			return resp
			# 	else:
			# 		resp = jsonify({'message' : 'rotation degree is not a valid number'})
			# 		resp.status_code = 400
			# 		return resp
		

		transformationsArray = transformationsValue.split(',')
		#for i in transformationsArray:
			#if(i not in ALLOWED_TRANSFORMATIONS):
				#resp = jsonify({'message' : 'Allowed transformations are: anticlockwise,clockwise,fliphorizontal,flipvertical,resize,rotate,grayscale,thumbnail '})
				#resp.status_code = 400
				#return resp	

	
		#call ImageTransformationsDecider to apply valid transformations
		for i in transformationsArray:
			#if(i in ALLOWED_TRANSFORMATIONS):
				temp = ImageTransformationsDecider(img, i)
				img = temp.applyTransformation(img, i)
	
		rawBytes = io.BytesIO()
		img.save(rawBytes, fileExtension)
		rawBytes.seek(0)

				#img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return send_file(rawBytes, mimetype='image/'+fileExtension)
			

	else:
		resp = jsonify({'message' : 'Allowed file types are png, jpg, jpeg'})
		resp.status_code = 400
		return resp


if __name__ == "__main__":
    app.run()