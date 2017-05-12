from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line import Line

class ProxRectAnalizer:


	def __init__ (self):
		'''

		
		[description]
		'''

	@staticmethod
	def groups (rects, filters=[]):
		'''[summary]
		
		[description]
		'''



		rects = ProxRectAnalizer.filter(rects, filters)

		###


	def filter (rects, filters = []):
		for filter in filters:

			for i in range(len(rects)-1, 0, -1):
				if filter.toFilter(rects[i]):
					rects.pop(i)

		return rects