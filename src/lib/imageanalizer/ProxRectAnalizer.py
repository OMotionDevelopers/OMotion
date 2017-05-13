from lib.geometry2d.polygons.Rectangle import Rectangle

from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line import Line

from lib.imageanalizer.filters.Filter import Filter


class ProxRectAnalizer:


	@staticmethod
	def groups (rects = [], filters = []):
		'''[summary]
		
		[description]
		'''



		rects = ProxRectAnalizer.filter(rects, filters)

		###


	@staticmethod
	def filter (rects = [], filters = []):
		'''this function add all rect matches filter
		
		for each rect, aplly filter
		
		Returns:
			[] -- array of filtered rects
		'''

		if not isinstance(rects, list):
			raise ValueError('invalid rects list, got: ' + str(type(rects)))

		for r in rects:
			if not isinstance(r, Rectangle):
				raise ValueError('Invalid rect, got: ' + str(type(r)))

		if not isinstance(filters, list):
			raise ValueError('invalid filters list, got: ' + str(type(filters)))

		for f in filters:
			if not isinstance(f, Filter):
				raise ValueError('Invalid filter, got: ' + str(type(f)))

		toReturn = []

		for r in rects:
			for f in filters:
				if f.toFilter(r):
					toReturn.append(r)

		return toReturn