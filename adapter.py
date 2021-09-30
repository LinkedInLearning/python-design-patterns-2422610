class Korean:
	"""Korean speaker"""
	def __init__(self):
		self.name = "Korean"

	def speak_korean(self):
		return "An-neyong?"

class British:
	"""English speaker"""
	def __init__(self):
			

	#Note the different method name here!
	def speak_english(self):
			

class Adapter:
	"""This changes the generic method name to individualized method names"""

	def __init__(self, object, **adapted_method):
		"""Change the name of the method"""
		self._object

		#Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
		#For example, speak() will be translated to speak_korean() if the mapping says so
		

	def __getattr__(self, attr):
		"""Simply return the rest of attributes!"""
		
		
#List to store speaker objects
objects = []

#Create a Korean object


#Create a British object


#Append the objects to the objects list


for obj in objects:
	print("{} says '{}'\n".format(obj.name, obj.speak()))

