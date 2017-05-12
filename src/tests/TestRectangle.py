from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.geometry2d.simple.Point import Point
from lib.geometry2d.simple.Line import Line


import unittest

class TestRectangle (unittest.TestCase):

	def setUp(self):

		pass

	def tearDown(self):
		pass


	def test_center (self):
		r = Rectangle(Point(0,0),10,10)
		p = Point(5,5)
		self.assertEqual(r.center(), p)


	def test_diagonal (self):
		r = Rectangle(Point(0,0), 10, 10)
		d = Line(Point(0,0), Point(10,10))
		self.assertEqual(r.diagonal(), d) 


	def test_points (self):
		r = Rectangle(Point(0,0), 1, 1)
		p = [
			Point(0,0),
			Point(1,0),
			Point(1,1),
			Point(0,1)
		]

		x = r.points()

		self.assertEqual(len(x), len(p))

		for i in range(len(x)):
			self.assertEqual(x[i],p[i])


	def test_edges (self):
		r = Rectangle(Point(0,0), 1, 1)
		l = [
			Line(Point(0, 0), Point(1, 0)),
			Line(Point(1, 0), Point(1, 1)),
			Line(Point(1, 1), Point(0, 1)),
			Line(Point(0, 1), Point(0, 0)),
		]

		x = r.edges()

		self.assertEqual(len(x), len(l))

		for i in range(len(x)):
			self.assertEqual(x[i], l[i])


	def test_edges_2 (self):
		r = Rectangle(Point(0,0), 1, 1)
		l = [
			Line(Point(0, 0), Point(1, 0)),
			Line(Point(1, 1), Point(1, 0)),
			Line(Point(0, 1), Point(1, 1)),
			Line(Point(0, 0), Point(0, 1)),
		]

		x = r.edges()

		self.assertEqual(len(x), len(l))

		for i in range(len(x)):
			self.assertEqual(x[i], l[i])


	def test_length (self):
		l = Line(Point(0,0), Point(0,1))

		self.assertEqual(l.length(), 1)