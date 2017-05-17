from lib.geometry2d.polygons.RotatedRectangle import RotatedRectangle

class ContoursRotatedRectangle (RotatedRectangle):

	contour = None

	def __init__ (self, contour, point, width, height, angle):

		self.contour = contour
		super().__init__(point, width, height, angle)


	@staticmethod
	def fromCv (contours, t):
		r = RotatedRectangle.fromCv(t)
		return ContoursRotatedRectangle(contours, r.point, r.width, r.height, r.angle)