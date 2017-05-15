import cv2

class VideoController:

	window = 'unnamed'

	def __init__ (self, window):
		'''

		'''

		self.window = window


	def analize(self):
		return

	def show (self, frame, name=None):
		if name is None:
			name = self.window

		cv2.imshow(name, frame)
		cv2.waitKey(1)

