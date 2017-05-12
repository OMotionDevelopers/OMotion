from lib.geometry2d.simple.Point import Point

import math


class Line:
	'''[summary]
	
	[description]
	'''

	p0 = None
	p1 = None

	def __init__ (self, p0, p1):
		'''[summary]
		
		[description]
		'''

		if not isinstance(p0, Point):
			raise ValueError('invalid start point type')

		if not isinstance(p1, Point):
			raise ValueError('invalid stop point type')		


		self.p0 = p0
		self.p1 = p1


	def __eq__ (self, other):
		'''return true if point are in the same position
		
		[description]
		'''
		return self.p0 == other.p0 and self.p1 == other.p1 or self.p0 == other.p1 and self.p1 == other.p0


	def center (self):
		'''[summary]
		
		[description]
		''' 

		return Point((self.p0.x + self.p1.x)/2, (self.p0.y + self.p1.y)/2)


	def intersection (self, other):
		'''[summary]
		#FIXME
		[description]
		''' 

		if not self.intersect(other):
			return None

		return 


	def intersect (self, other):
		'''[summary]
		#FIXME	
		[description]
		'''
		
		return False


	def angleBetween (self, other):
		'''[summary]
		#FIXME
		[description]
		'''
		return 0


	def length (self):
		'''
		
		[description]
		'''

		return math.sqrt((self.p0.x - self.p1.x)**2 + (self.p0.y - self.p1.y)**2)