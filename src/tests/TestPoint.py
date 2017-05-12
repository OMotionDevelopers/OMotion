from lib.geometry2d.simple.Point import Point

import unittest
import math

class TestPoint (unittest.TestCase):

	def setUp(self):
		#
		pass

	def tearDown(self):
		#
		pass

	def test_valid_coordinate(self):
		Point(3,4.4)

	def test_invalid_coordinate(self):
		with self.assertRaises(ValueError):
			Point('foo',[1,2,34])

	def test_polar_coordinate(self):
		a = Point(0,0)
		b = a.polar(1,0)
		c = Point(1,0)

		self.assertEqual(b,c)

	def test_polar_coordinate_2 (self):
		a = Point(0,0)
		b = a.polar(0,0)

		self.assertEqual(a,b)

	def test_polar_coordinate_3 (self):
		a = Point(0,0)
		b = a.polar(-1, 0)
		c = Point(-1,0)

		self.assertEqual(b,c)

	def test_polar_coordinate_4 (self):
		a = Point(1,1)
		b = a.polar(1,math.pi/2)
		c = Point(1,2)

		self.assertEqual(b,c)

