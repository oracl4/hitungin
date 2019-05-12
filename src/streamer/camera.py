import numpy as np
import cv2 
import imutils

class Camera(object):
	def __init__(self):
		self.cap = cv2.VideoCapture("/home/oracl4/project/hitungin/input/input.mp4")
		self.cap1 = cv2.VideoCapture(0)
		
	def get_frame(self):
		ret, frame = self.cap.read()

		if ret == False:
			ret, frame = self.cap1.read()

		frame = imutils.resize(frame, width=500)
		formated_data = cv2.imencode('.jpeg', frame)[1]
		frame_bytes = formated_data.tobytes()
		
		return frame_bytes

	def __del__(self):
		self.cap.release()
		self.cap1.release()
		
