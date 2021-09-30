class DrawingAPIOne(object):
	"""Implementation-specific abstraction: concrete class one"""
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
	"""Implementation-specific abstraction: concrete class two"""
	
		

class Circle(object):
	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""

	def __init__(self, x, y, radius, drawing_api):
		"""Initialize the necessary attributes"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation-specific abstraction taken care of by another class: DrawingAPI"""
		

	def scale(self, percent):
		"""Implementation-independent"""
		self._radius *= percent


#Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw a circle
circle1.draw()

#Build the second Circle object using API Two

#Draw a circle


