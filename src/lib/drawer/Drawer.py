import cv2

class Drawer:

	@staticmethod
	def drawPolygon(frame, polygon, color, size):
		edges = polygon.edges()

		for e in edges:
			cv2.line(frame, e.p0.toCv(), e.p1.toCv(), color, size)


	@staticmethod
	def drawPolygons(frame, polygons, color, size):
		for polygon in polygons:
			Drawer.drawPloygon(frame, polygon, color, size)


	@staticmethod
	def drawContour(frame, contour, color, size):
		cv2.drawContours(frame, [contour], 0, color, size)

