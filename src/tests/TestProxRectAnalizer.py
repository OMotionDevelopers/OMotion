from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line import Line

from lib.imageanalizer.ProxRectAnalizer    import ProxRectAnalizer
from lib.imageanalizer.filters.RectAreaFilter import RectAreaFilter


import unittest

class TestProxRectAnalizer (unittest.TestCase):

	def test_filters (self):

		r = [
			Rectangle(Point(0,0), 10, 10), #100
			Rectangle(Point(0,0), 20, 20), #400
			Rectangle(Point(0,0), 30, 30), #900
			Rectangle(Point(0,0), 40, 40), #1600
			Rectangle(Point(0,0), 50, 50), #2500
		]

		f = RectAreaFilter(150, 950)


		s = ProxRectAnalizer.filter(r, [f])

		for i in s:
			print(i)

		self.assertEqual(s[0], Rectangle(Point(0,0), 20, 20))
		self.assertEqual(s[1], Rectangle(Point(0,0), 30, 30))
