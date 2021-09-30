import types #Import the types module

class Strategy:
    """The Strategy Pattern class"""
    
    def __init__(self, function=None):
        self.name = "Default Strategy"
        
        #If a reference to a function is provided, replace the execute() method with the given function
        
            
    def execute(self): #This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))

#Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

#Replacement method 2    
def strategy_two(self):
	
    
#Let's create our default strategy
s0 = 
#Let's execute our default strategy
s0.execute()

#Let's create the first varition of our default strategy by providing a new behavior
s1 = 
#Let's set its name
s1.name = 
#Let's execute the strategy
s1.

s2 = 
s2.name = 
s2.

