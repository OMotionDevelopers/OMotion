import math

class Converter:

	@staticmethod
	def degrees2radians (degrees):
		return math.pi * degrees / 180

	@staticmethod
	def radians2degrees (radians):
		return 180 * radians / math.pi