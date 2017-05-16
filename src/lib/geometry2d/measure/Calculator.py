from lib.geometry2d.simple.Point import Point

import math

class Calculator:

	@staticmethod
	def polar(point, distance, angle):
		return Point(point.x + distance * math.cos(angle), point.y + distance * math.sin(angle))