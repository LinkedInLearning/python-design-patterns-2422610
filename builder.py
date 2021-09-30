class Director():
    """Director"""
    def __init__(self, builder):
        self._builder = builder 
        
    def construct_car(self):
        
        
    def get_car(self):
        
        
        
 
class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None 
        
    def create_new_car(self):
        self.car = Car()
        


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """
    
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    


class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


