import math

class Point:

	x = None
	y = None


	def __init__ (self, x, y):
		'''[summary]
		
		[description]
		
		Raises:
			ValueError -- [description]
			ValueError -- [description]
		'''

		if not isinstance(x, float) and not isinstance(x, int):
			raise ValueError('Not a valid x coordinate')


		if not isinstance(y, float) and not isinstance(y, int):
			raise ValueError('Not a valid x coordinate')

		self.x = x
		self.y = y


	def __del__ (self):
		'''[summary]
		
		[description]
		'''
		pass


	def __eq__ (self, other):
		'''return true if point are in the same position
		
		[description]
		'''
		return self.x == other.x and self.y == other.y

	def __str__ (self):
		'''		
		return info & contents of Point
		
		Returns:
			string -- object string signature value
		'''
		return Point.__name__ + '(' + \
			'x: ' + str(self.x) + ', ' + \
			'y: ' + str(self.y)        + \
			')' #

	def polar (self, distance, angle):
		'''[summary]
		
		[description]
		'''
		
		x = self.x + distance * math.cos(angle)
		y = self.y + distance * math.sin(angle)
		
		return Point(x,y)


	def sumcpy (self, offsetx, offsety):
		return Point(self.x + offsetx, self.y+offsety)


	def toCv(self):
		return (int(self.x), int(self.y))