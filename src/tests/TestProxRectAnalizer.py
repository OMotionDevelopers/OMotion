from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line import Line

from lib.imageanalizer.ProxRectAnalizer    import ProxRectAnalizer
from lib.imageanalizer.filters.RectAreaFilter import RectAreaFilter


import unittest

class TestProxRectAnalizer (unittest.TestCase):

	def test_filter (self):

		f = RectAreaFilter(150, 950)

		r = [
			Rectangle(Point(0,0), 10, 10), #100  -- no
			Rectangle(Point(0,0), 20, 20), #400  -- yes
			Rectangle(Point(0,0), 30, 30), #900  -- yes
			Rectangle(Point(0,0), 40, 40), #1600 -- no
			Rectangle(Point(0,0), 50, 50), #2500 -- no
		]


		s = ProxRectAnalizer.filter(r, [f])

		self.assertIn(Rectangle(Point(0,0), 20, 20), s)
		self.assertIn(Rectangle(Point(0,0), 30, 30), s)


	def test_multiple_filter (self):

		f = RectAreaFilter (300, 500)
		g = RectAreaFilter (800, 950)

		r = [
			Rectangle(Point(0,0), 10, 10), #100  -- no
			Rectangle(Point(0,0), 20, 20), #400  -- yes (in f)
			Rectangle(Point(0,0), 30, 30), #900  -- yes (in g)
			Rectangle(Point(0,0), 40, 40), #1600 -- no
			Rectangle(Point(0,0), 50, 50), #2500 -- no
		]

		s = ProxRectAnalizer.filter(r, [f,g])

		self.assertIn(Rectangle(Point(0,0), 20, 20), s)
		self.assertIn(Rectangle(Point(0,0), 30, 30), s)

