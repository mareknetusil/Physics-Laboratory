def Print_Wrong_Dimensions():
    print("Different Vector dimensions")

def Print_Not_Vector():
    print("One of the arguments is not a vector")


class Vector():
    def __init__(self, list_values):
        self.values = list_values
        self.dim = len(list_values)
    

    def __mul__(self, v):
        if isinstance(v, Vector):
            if self.dim == v.dim:
                inner = 0.0
                for i,_ in enumerate(self.values):
                    inner += self.values[i]*v.values[i]
                    return inner
            else:
                Print_Wrong_Dimensions()
        else:
            try:
                return Vector([value*float(v) for value in self.values])
            except:
                print("Vector can be multiplied only by a scalar number or another Vector")
                
    def __rmul__(self, u):
        return self.__mul__(u)
    
    def __add__(self, v):
        if isinstance(v, Vector):
            if self.dim == v.dim:
                return Vector([self.values[i]+v.values[i] for i,_ in enumerate(self.values)])
            else:
                Print_Wrong_Dimensions()
        else:
            Print_Not_Vector()
            
    def __radd__(self, u):
        return self.__add__(u)
    
    
    def __sub__(self, v):
        return self+(-1)*v
    
    