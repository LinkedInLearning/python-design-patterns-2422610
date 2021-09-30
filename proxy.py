import time

class Producer:
	"""Define the 'resource-intensive' object to instantiate!"""
	def produce(self):
		print("Producer is working hard!")

	def meet(self):
		print("Producer has time to meet you now!")

class Proxy:
	""""Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
	def __init__(self):  
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		"""Check if Producer is available"""
		print("Artist checking if Producer is available ...")

		if self.occupied == 'No':
			#If the producer is available, create a producer object!
			

			#Make the prodcuer meet the guest!
			
			
		else:
			#Otherwise, don't instantiate a producer 
			time.sleep(2)
			print("Producer is busy!")

#Instantiate a Proxy


#Make the proxy: Artist produce until Producer is available


#Change the state to 'occupied'


#Make the Producer produce


