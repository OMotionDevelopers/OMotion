import cv2

class Drawer:

	@staticmethod
	def draw(frame, polygon, color, size):
		edges = polygon.edges()

		for e in edges:
			cv2.line(frame, e.p0.toCv(), e.p1.toCv(), color, size)
