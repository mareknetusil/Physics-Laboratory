from algebra import Vector

class gravity_field_homogeneous():
    def __init__(self, g, direction):
        self.g = g
        self.direction = Vector(direction)
        
    def __call__(self, objects):
        if objects != []:
            return [mass_object.mass*self.g*self.direction for mass_object in objects]
        

class ground():
    def __init__(self, relation, n): 
        self.relation = relation
        self.n = n
        
    def __call__(self, objects, displacements):
        new_coors = [o.coors + u for o, u in zip(objects, displacements)]
        for i, o in enumerate(objects):
            if not self.relation(new_coors[i]):
                displacements[i] = 0*displacements[i]
                o.velocity = (-1.0)*o.velocity
        
    

class Mass_Point():
    def __init__(self, coors, velocity, acceleration, mass):
        self.coors = Vector(coors)
        self.velocity = Vector(velocity)
        self.acceleration = Vector(acceleration)
        self.mass = mass
        self.dim = self.coors.dim
        

class System():
    def __init__(self, objects, forces = None, constrains = None):
        self.objects = objects
        self.dim = objects[0].dim
        self.num_objects = len(objects)
        self.forces = forces if forces else []
        self.constrains = constrains if constrains else []
        
    def add_object(self, objects):
        self.objects += objects
        self.num_objects += len(objects)
        
    def remove_object(self, index_list):
        for i in index_list:
            self.objects[i].pop()
        
    def move(self, displacements):
        for i in range(self.num_objects):
            self.objects[i].coors += displacements[i]
            
    def compute_displacements(self, dt):
        return [o.velocity*dt + 0.5*o.acceleration*dt**2 for o in self.objects]
    
    def update_velocity(self, dt):
        for o in self.objects:
            o.velocity += o.acceleration*dt 
    
    def update_acceleration(self, dt):
        tF = self.total_force()
        for i, o in enumerate(self.objects):
            o.acceleration = (1.0/o.mass)*tF[i]
        
    def total_force(self):
        zero_vec = Vector([0.0,0.0]) if self.dim == 2 else Vector([0.0,0.0,0.0])
        tF = [zero_vec for i in range(self.num_objects)]
        for force in self.forces:
            tF = [tF[i] + force(self.objects)[i] for i in range(self.num_objects)]
        return tF
    
    def step_next(self, dt):
        self.update_acceleration(dt)
        self.update_velocity(dt)
        u = self.compute_displacements(dt)
        for constraint in self.constrains:
            constraint(self.objects, u)
        self.move(u)
        
        
class Simulation():
    def __init__(self, systems, dt):
        self.systems = systems
        self.dt = dt
        
    def step_next(self):
        for system in self.systems:
            system.step_next(self.dt)