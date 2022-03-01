from math import sqrt

def magnitude(vector):
    x_squared = vector.x * vector.x
    y_squared = vector.y * vector.y
    z_squared = vector.z * vector.z
    w_squared = vector.w * vector.w
    return sqrt(x_squared + y_squared + z_squared + w_squared)

def normalize(vector):
    mag = magnitude(vector)
    return Tuple(vector.x/mag, vector.y/mag, vector.z/mag, vector.w/mag)

def dot_product(vector_a, vector_b):
    x_prod = vector_a.x * vector_b.x
    y_prod = vector_a.y * vector_b.y
    z_prod = vector_a.z * vector_b.z
    w_prod = vector_a.w * vector_b.w

    return x_prod + y_prod + z_prod + w_prod

def cross_product(vector_a, vector_b):
    new_x = vector_a.y * vector_b.z - vector_a.z * vector_b.y
    new_y = vector_a.z * vector_b.x - vector_a.x * vector_b.z
    new_z = vector_a.x * vector_b.y - vector_a.y * vector_b.x
    return Vector(new_x, new_y, new_z)

class Tuple:
    def __init__(self, x, y, z, w):
        self._x = x
        self._y = y
        self._z = z
        self._w = w
    
    def __repr__(self):
        return f"x:{self._x}, y:{self._y}, z:{self._z}, w:{self._w}"

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z
    
    @property
    def w(self):
        return self._w
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        new_w = self.w + other.w

        return Tuple(new_x, new_y, new_z, new_w)
    
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        if self.is_point():
            if other.is_point():
                return Vector(new_x, new_y, new_z)
            elif other.is_vector():
                return Point(new_x, new_y, new_z)
        elif self.is_vector():
            if other.is_vector():
                return Vector(new_x, new_y, new_z)
    
    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __eq__(self, other):
        x_equals = round(self.x, 5) == round(other.x, 5)
        y_equals = round(self.y, 5) == round(other.y, 5)
        z_equals = round(self.z, 5) == round(other.z, 5)
        w_equals = self.w == other.w
        
        return x_equals and y_equals and z_equals and w_equals
    
    def __mul__(self, other):
        return Tuple(self.x * other, self.y * other, self.z * other, self.w * other)
    
    def __truediv__(self, other):
        """
            divides by scalar and fraction
        """
        return Tuple(self.x/other, self.y/other, self.z/other, self.w/other)
    
    def is_point(self):
        return self.w == 1.0
    
    def is_vector(self):
        return self.w == 0.0

    
class Point(Tuple):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self._w = 1.0

class Vector(Tuple):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self._w = 0.0