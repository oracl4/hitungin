import numpy as np
import cv2 
class Camera(object):
	def __init__(self):
		self.cap = cv2.VideoCapture("dte123.avi")
		#self.cap.set(3,240)
		#self.cap.set(4,320)
		
	def get_frame(self):
		ret, frame = self.cap.read()
		formated_data = cv2.imencode('.jpeg', frame)[1]
		frame_bytes = formated_data.tobytes()
		if(frame_bytes==null)
			return frame_bytes
		elif
			return frame_bytes

	def __del__(self):
		self.cap.release()