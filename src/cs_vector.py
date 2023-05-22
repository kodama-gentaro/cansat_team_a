class Vector:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=None, y=None, z=None, tuple_vector : tuple=None):
        if tuple_vector is None and x is not None and y is not None and z is not None:
            self.x = x
            self.y = y
            self.z = z
        elif tuple_vector is not None and x is y is z is None:
            if len(tuple_vector) == 3:
                self.x = tuple_vector[0]
                self.y = tuple_vector[1]
                self.z = tuple_vector[2]
    def get_tuple(self):
        tuple_vector = self.x, self.y, self.z
        return tuple_vector

    def set_vector(self, x=None, y=None, z=None):
        self.x = x if x is not None else self.x
        self.y = y if y is not None else self.y
        self.z = z if z is not None else self.z

