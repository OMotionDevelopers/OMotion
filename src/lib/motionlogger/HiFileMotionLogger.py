from lib.motionlogger.MotionLogger import MotionLogger
from lib.geometry2d.polygons.Rectangle import Rectangle
from lib.imageanalizer.filters.Filter import Filter

import os
import time
import datetime

class HiFileMotionLogger (MotionLogger):

	FILE_PATH 	= 	os.getcwd()+'/../log/motion.log'
	log 		= 	None
	logTime 	= 	None


	def __init__ (self):
		'''
		method which give the possibility of open a file (motion.log) in order to 
		write on it the motions detected
		'''	


	def __del__ (self):
		'''
		close the file writed
		'''

		if self.log:
			os.close(self.log)


	def getTime(self):
		return datetime.datetime.now().strftime('%d.%m.%Y - %H:%M:%S')



	def logRotatedRect(self, rects):
		out = self.getTime() + '\n'

		for rect in rects:
			o = str(rect.center()) 	#motion's origin point
			a = str(rect.area())	#string for evidentiation of motion area size

			out += 'Movimento di area ' + a + ' a partire dall\'origine ' + o +'\n'

		
		with open(self.log) as file:
			file.write(out)
		# os.write(self.log, out.encode('utf-8'))
		


