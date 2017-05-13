from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.geometry2d.simple.Point       import Point

from lib.imageanalizer.filters.RectAreaFilter import RectAreaFilter

import unittest

class TestAreaFilter (unittest.TestCase):

	f = None
	MIN = 9
	MAX = 100

	def setUp (self):
		#
		#
		#
		self.f = RectAreaFilter(TestAreaFilter.MIN, TestAreaFilter.MAX)


	def tearDown (self):
		#
		#
		#
		del self.f
		self.f = None


	def test_lower_area_rect (self):
		# check rectangle of area 1x1 < 9
		# should return false
		r = Rectangle(Point(0,0), 1, 1) # area = 1 x 1 = 1
		self.assertFalse(self.f.toFilter(r))

	def test_upper_area_rect (self):
		# check rectangle of area 11x11 > 100
		# should return false
		r = Rectangle(Point(0,0), 11, 11) # area = 11 x 11 = 121
		self.assertFalse(self.f.toFilter(r))

	def test_inside_area_rect (self):
		# check rectangle of area 5x5 > 9, < 100
		# should return true
		r = Rectangle(Point(0,0), 5, 5) # area = 5 x 5 = 25
		self.assertTrue(self.f.toFilter(r))

	def test_lower_bound_area_rect (self):
		# check rectangle of area 3x3 = 9
		# should return true
		r = Rectangle(Point(0,0), 3, 3) # area = 3 x 3 = 9
		self.assertTrue(self.f.toFilter(r))

	def test_upper_bound_area_rect (self):
		# check rectangle of area 10x10 = 100
		# should return true
		r = Rectangle(Point(0,0), 10, 10) # area = 10 x 10 = 100
		self.assertTrue(self.f.toFilter(r))