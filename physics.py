from algebra import Vector

def gravity_field_homogeneous(objects, **kwargs):
    if objects != []:
        g = kwargs['g']
        direction = kwargs['direction']
        return [mass_object.mass*g*direction for mass_object in objects]
        
    

class Mass_Point():
    def __init__(self, coors, velocity, acceleration, mass):
        self.coors = Vector(coors)
        self.velocity = Vector(velocity)
        self.acceleration = Vector(acceleration)
        self.mass = mass
        

class System():
    def __init__(self, objects, forces = None):
        self.objects = objects
        self.num_objects = len(objects)
        self.forces = forces if forces else []
        
    def add_object(self, objects):
        self.objects += objects
        self.num_objects += len(objects)
        
    def remove_object(self, index_list):
        for i in index_list:
            self.objects[i].pop()
        
    def move(self, displacements):
        for i in self.num_objects:
            self.objects[i].coors += displacements[i]
            
    def compute_displacements(self, dt):
        return [o.velocity*dt + 0.5*o.acceleration*dt**2 for o in self.objects]
    
        
        
class Simulation():
    def __init__(self, systems, dt):
        self.systems = systems
        self.dt = dt
        
    def step_next(self):
        pass