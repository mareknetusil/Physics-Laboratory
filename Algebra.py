def Print_Wrong_Dimensions():
    print("Different Vector dimensions")

def Print_Not_Vector():
    print("One of the arguments is not a vector")
    
def kronecker_delta(i,j):
    return 1.0 if i == j else 0.0

def levi_civita(i,j,k):
    if i == j or j == k or i == k:
        return 0.0
    return 1.0 if (i,j,k) in [(1,2,3),(2,3,1), (3,1,2)] else -1.0


class Vector():
    @staticmethod
    def dim_equality(u,v):
        if u.dim == v.dim:
            return True
        else:
            Print_Wrong_Dimensions()
            return False

    def __init__(self, list_values):
        self.values = list_values
        self.dim = len(list_values)
    

    def __mul__(self, v):
        if isinstance(v, Vector):
            if Vector.dim_equality(self, v):
                inner = 0.0
                for i,_ in enumerate(self.values):
                    inner += self.values[i]*v.values[i]
                    return inner
        else:
            try:
                return Vector([value*float(v) for value in self.values])
            except:
                print("Vector can be multiplied only by a scalar number or another Vector")
                
    def __rmul__(self, u):
        return self.__mul__(u)
    
    def __add__(self, v):
        if isinstance(v, Vector):
            if Vector.dim_equality(self, v):
                return Vector([self.values[i]+v.values[i] for i,_ in enumerate(self.values)])
        else:
            Print_Not_Vector()
            
    def __radd__(self, u):
        return self.__add__(u)
    
    
    def __sub__(self, v):
        return self+(-1)*v
    
    def __pow__(self, v):
        if self.dim == 3:
            if Vector.dim_equality(u, v):
                return Vector([])
        else:
            print("Vector product is implemented only for dimension == 3") 
    
    