from lib.videocontroller.VideoController import VideoController

from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.geometry2d.polygons.RotatedRectangle import RotatedRectangle

from lib.geometry2d.composite.ContoursRotatedRectangle import ContoursRotatedRectangle

from lib.imageanalizer.ProxRectAnalizer import ProxRectAnalizer

from lib.imageanalizer.filters.RectAreaFilter import RectAreaFilter

from lib.drawer.Drawer import Drawer

from lib.motionlogger.FileMotionLogger import FileMotionLogger
from lib.motionlogger.HiFileMotionLogger import HiFileMotionLogger

import cv2
import numpy as np
import copy

class CameraController (VideoController):
	'''
	
	'''

	camera = None
	device = 0
	kernel = None
	oldcnt = []
	lastcnt = None
	rrmotion = None
	colors = [
		( 88,  24,  89),
		(144,  12,  63),
		(199,   9,  57),
		(255,  87,  51),
		(255, 195,   0)
	]
	logger = None

	filters = None

	backsub = cv2.createBackgroundSubtractorMOG2()
	backg   = None

	def __init__ (self):
		'''

		'''
		super().__init__('video')

		self.camera = cv2.VideoCapture(CameraController.device)
		self.kernel = np.ones((5,5))

		self.filters = [
			RectAreaFilter(150, 100000)
		]

		self.logger = FileMotionLogger()

		# self.colors = []
		# o = 127
		# for i in range(0, 255, o):
		# 	for j in range(0, 255, o):
		# 		for k in range(0, 255, o):
		# 			self.colors.append((i,j,k))

	def analize (self):

		while self.camera.isOpened():
			self.rrmotion = []

			ret, frame = self.camera.read()
			# frame2 = copy.copy(frame)

			frame2 = np.zeros(frame.shape, dtype=np.uint8)
			frame3 = np.zeros(frame.shape, dtype=np.uint8)




			self.motionsearch(frame)
			# self.motiondraw(frame2)
			
			#self.rrmotion e una lista che contiene i rettangoli del movimento per questo frame

			self.drawContoursHistory(frame2)
			self.drawPolygonsMotion(frame3)

			if self.rrmotion:
				self.logger.logRotatedRect(self.rrmotion)


			# for rr in self.rrmotion:
			# 	Drawer.drawPolygon(frame, rr, (0,255,0)  , 2)
			# 	break

			self.show(np.hstack((frame,frame2,frame3)))
			self.show(self.backg, name='backg')


	def motionsearch (self, frame):

		self.backg = self.backsub.apply(frame)

		ret, self.backg = cv2.threshold(self.backg, 250,255, cv2.THRESH_BINARY)

		# self.backg = cv2.erode(self.backg, self.kernel)
		self.backg = cv2.morphologyEx(self.backg, cv2.MORPH_OPEN, self.kernel)

		_, cnt, h = cv2.findContours(self.backg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		self.addCnt(cnt)
		self.lastcnt = cnt

				# rs = []
		self.rrmotion = []

		for i in self.lastcnt:
			self.rrmotion.append(ContoursRotatedRectangle.fromCv(i,cv2.minAreaRect(i)))

			
		
		



	# def motiondraw (self, frame):

	# 	for cnt, color in zip(self.oldcnt, self.colors):
	# 		cv2.drawContours(frame, cnt, -1, color, 1)

	# 	rs = []
	# 	gs = []

	# 	for i in self.lastcnt:
	# 		r = cv2.minAreaRect(i)
	# 		gs.append(ContoursRotatedRectangle.fromCv(i,r))

	# 		r = cv2.boxPoints(r)
	# 		r = np.int0(r)

	# 		rs.append(r)
			

		

	# 	cv2.drawContours(frame, rs, -1, (255,255,255), 3)

	# 	for g in ProxRectAnalizer.filter(gs, self.filters):
	# 		Drawer.drawPolygon(frame, g,         (255,0,0)  , 2)
	# 		Drawer.drawContour(frame, g.contour, (0,0,255), 1)

		# for g in gs:
		# 	Drawer.draw(frame, g, (255,0,0), 2)


	def addCnt(self, cnt):
		self.oldcnt.insert(0, cnt)

		if len(self.oldcnt) > len(self.colors):
			self.oldcnt.pop()


	def drawContoursHistory (self, frame):
		for cnt, color in zip(self.oldcnt, self.colors):
	 		cv2.drawContours(frame, cnt, -1, color, 1)

	def drawPolygonsMotion (self, frame):

			
		# cv2.drawContours(frame, rs, -1, (255,255,255), 3)

		for g in ProxRectAnalizer.filter(self.rrmotion, self.filters):
			Drawer.drawPolygon(frame, g,         (255,0,0)  , 2)
			Drawer.drawContour(frame, g.contour, (0,0,255), 1)

		# for g in gs:
		# 	Drawer.draw(frame, g, (255,0,0), 2)