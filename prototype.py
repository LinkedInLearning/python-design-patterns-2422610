import copy

class Prototype:
    
    def __init__(self):
        
        
    def register_object(self, name, obj):
        """Register an object"""
        
        
    def unregister_object(self, name):
        """Unregister an object"""
        
        
    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        
        
class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
        



