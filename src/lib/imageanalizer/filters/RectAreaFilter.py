from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line import Line

from lib.imageanalizer.filters.Filter import Filter

class RectAreaFilter (Filter):


	minarea = 0
	maxarea = 0

	def __init__ (self, minarea, maxarea):
		'''
		filter rects by area, valid only if minarea < rect.area < maxarea
		
		[description]
		'''
		self.minarea = minarea
		self.maxarea = maxarea

	
	def toFilter (self, rect):
		'''[summary]
		
		[description]
		'''
		
		if not isinstance(rect, Rectangle):
			raise ValueError('Invalid filter parameter, must be of type: ' + Rectangle.__module__ + '.' + Rectangle.__name__ + ', got: ' + str(type(rect)))

		return True if self.minarea <= rect.area() and rect.area() <= self.maxarea else False


