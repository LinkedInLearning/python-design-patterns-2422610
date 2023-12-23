class Dog:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"

class Cat:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"	
	
def get_pet(pet="cat"):
	"""The factory method """
	pets = dict(dog=Dog("Ko"), cat=Cat("Ka"))
	return pets[pet]

d = get_pet("dog")
print(d.speak())