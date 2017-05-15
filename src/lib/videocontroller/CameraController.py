from lib.videocontroller.VideoController import VideoController

import cv2
import numpy as np

class CameraController (VideoController):
	'''

	'''

	camera = None
	device = 0
	kernel = None
	oldcnt = []
	lastcnt = None
	colors = [
		( 88,  24,  89),
		(144,  12,  63),
		(199,   9,  57),
		(255,  87,  51),
		(255, 195,   0)
	]

	backsub = cv2.createBackgroundSubtractorMOG2()

	def __init__ (self):
		'''

		'''
		super().__init__('video')

		self.camera = cv2.VideoCapture(CameraController.device)
		self.kernel = np.ones((5,5))

		self.colors = []
		o = 127
		for i in range(0, 255, o):
			for j in range(0, 255, o):
				for k in range(0, 255, o):
					self.colors.append((i,j,k))

	def analize (self):

		while self.camera.isOpened():

			ret, frame = self.camera.read()

			self.motionsearch(frame)
			self.motiondraw(frame)

			self.show(frame)


	def motionsearch (self, frame):

		mask = self.backsub.apply(frame)

		ret, mask = cv2.threshold(mask, 127,255, cv2.THRESH_BINARY)

		mask = cv2.erode(mask, self.kernel)

		_, cnt, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		self.addCnt(cnt)
		self.lastcnt = cnt

		
		



	def motiondraw (self, frame):

		for cnt, color in zip(self.oldcnt, self.colors):
			cv2.drawContours(frame, cnt, -1, color, 1)

		for i in self.lastcnt:
			r = cv2.minAreaRect(i)
			r = cv2.boxPoints(r)
			r = np.int0(r)
			cv2.drawContours(frame, [r], 0, (255,255,255), 3)


	def addCnt(self, cnt):
		self.oldcnt.insert(0, cnt)

		if len(self.oldcnt) > len(self.colors):
			self.oldcnt.pop()
