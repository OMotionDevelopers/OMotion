from lib.geometry2d.polygons.Rectangle import Rectangle

from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line import Line

from lib.geometry2d.measure.Calculator import Calculator
from lib.geometry2d.measure.Converter import Converter

import numbers

class RotatedRectangle (Rectangle):
	'''

	'''

	angle = 0

	def __init__ (self, point, width, height, angle):
		'''

		'''
		
		super().__init__(point, width, height)

		if not isinstance(angle, numbers.Number):
			raise ValueError('Invalid angle type')

		self.angle = angle


	@staticmethod
	def fromCv (t):
		'''

		'''
		point, size, angle = t

		if not isinstance(point, tuple)             or \
		   not len(point) == 2                      or \
		   not isinstance(point[0], numbers.Number) or \
		   not isinstance(point[1], numbers.Number)    :
			raise ValueError('Invalid Point parameter')

		if not isinstance(size, tuple)             or \
		   not len(size) == 2                      or \
		   not isinstance(size[0], numbers.Number) or \
		   not isinstance(size[1], numbers.Number)    :
			raise ValueError('Invalid Size parameter')

		if not isinstance(angle, numbers.Number):
			raise ValueError('Invalid Angle Parameter')

		return RotatedRectangle(Point(point[0], point[1]).polar(-(size[1]/2), Converter.degrees2radians(angle-90)).polar(size[0]/2, Converter.degrees2radians(angle-180)), size[0], size[1], Converter.degrees2radians(angle-90))


	def __lt__ (self, other):
		if not isinstance(other, Rectangle): return NotImplemented
		return self.area() < other.area()

	def __eq__ (self, other):
		if not isinstance(other, RotatedRectangle): return NotImplemented
		return super().__eq__(other) and self.angle == other.angle

	def __gt__ (self, other):
		if not isinstance(other, Rectangle): return NotImplemented
		return self.area() > other.area()


	def __str__ (self):
		'''

		'''

		return RotatedRectangle.__module__ + '.' + RotatedRectangle.__name__ + '(' + \
			'point: '   + str(self.point) + ',' + \
			'width: '   + str(self.width) + ',' + \
			'height: '  + str(self.height) + ',' + \
			'angle: '   + str(self.angle) + ',' + \
			')' #


	def center (self):
		'''

		'''

		pointhw = Calculator.polar(self.point, self.width/2, Converter.degrees2radians(self.angle))
		pointhh = Calculator.polar(pointhw   , self.height/2, Converter.degrees2radians(self.angle+90))

		return pointhh

	def diagonal (self):
		'''

		'''

		pass


	def points (self):
		'''

		'''

		a = self.point
		b = Calculator.polar(a, self.height, self.angle)
		c = Calculator.polar(b, self.width, Converter.degrees2radians(90) + self.angle)
		d = Calculator.polar(c, self.height, Converter.degrees2radians(180) + self.angle)

		return [
			a,
			b,
			c,
			d
		]
		

	def edges (self):
		'''

		'''
		p = self.points()

		return [
			Line(p[0], p[1]),
			Line(p[1], p[2]),
			Line(p[2], p[3]),
			Line(p[3], p[0])
		]