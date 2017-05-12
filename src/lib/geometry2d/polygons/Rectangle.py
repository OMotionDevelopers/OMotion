from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line  import Line

import numbers

class Rectangle:
	'''this class rapresent a generic rectangle polygon
	
	is placed in 2d space cartesian coordinates and operate
	with other object of 2d module
	'''

	point  = None
	width  = 0
	height = 0


	def __init__ (self, point, width, height):
		'''
				
		[description]
		
		Returns:
			number -- [description]
		'''

		if not isinstance(point, Point):
			raise ValueError('invalid point type')

		if not isinstance(width, numbers.Number):
			raise ValueError('invalid width type')

		if width < 0:
			raise ValueError('invalid width value')

		if not isinstance(height, numbers.Number):
			raise ValueError('invalid height type')

		if height < 0:
			raise ValueError('invalid height value')

		self.point  = point
		self.width  = width
		self.height = height
	

	def __eq__ (self, other):
		return self.point == other.point and self.width == other.width and self.height == other.height


	def __str__ (self):
		return 'point: (' + str(self.point.x) + ', ' + str(self.point.y) +'), width = ' + str(self.width) + ', height = ' + str(self.height) + ', area = ' + str(self.area())

	def center (self):
		'''[summary]
		
		[description]
		'''

		return Point(self.point.x + self.width/2, self.point.y + self.height/2)


	def diagonal (self):
		'''[summary]
		
		[description]
		'''

		return Line(Point(self.point.x, self.point.y), Point(self.point.x + self.width, self.point.y + self.height))


	def area (self):
		'''[summary]
		
		[description]
		'''

		
		return self.width * self.height


	def perimeter (self):
		'''[summary]
		
		[description]
		'''

		return (self.width * 2) + (self.height * 2)


	def points (self):
		'''[summary]
		
		[description]
		''' 

		
		return [
			self.point,
			self.point.sumcpy(self.width, 0),
			self.point.sumcpy(self.width, self.height),
			self.point.sumcpy(0, self.height)
		]

	
	def edges (self):
		'''[summary]
		
		[description]
		''' 


		return [
			Line(self.point, self.point.sumcpy(self.width, 0)),
			Line(self.point.sumcpy(self.width, 0), self.point.sumcpy(self.width, self.height)),			
			Line(self.point.sumcpy(self.width, self.height), self.point.sumcpy(0, self.height)),
			Line(self.point.sumcpy(0, self.height), self.point)
		]
