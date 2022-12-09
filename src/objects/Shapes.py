from Tuple import Point, dot_product
from Intersection import Intersection, Intersections
from math import sqrt


class Sphere:
    """
        The Sphere class has an origin which is a point and a radius which is a number
    """
    def __init__(self):
        self._origin = Point(0, 0, 0)
        self._radius = 1.0

    @property
    def origin(self):
        return self._origin

    @property
    def radius(self):
        return self._radius

    def intersect(self, ray):
        """
            given a ray see if it intersects with the sphere
            return an Intersections opbject
        """
        sphere_to_ray = ray.origin - self.origin
        a = dot_product(ray.direction, ray.direction)
        b = 2 * dot_product(ray.direction, sphere_to_ray)
        c = dot_product(sphere_to_ray, sphere_to_ray) - 1

        discriminant = b * b - 4 * a * c
        # does the ray ever even intersect the sphere?

        if discriminant < 0:
            return Intersections([])

        neg_b = b * -1
        t1 = (neg_b - sqrt(discriminant)) / (2 * a)
        t2 = (neg_b + sqrt(discriminant)) / (2 * a)
        I1 = Intersection(t1, self)
        I2 = Intersection(t2, self)

        return Intersections([I1, I2])

    def __eq__(self, other):
        origin_eq = other._origin == self._origin
        radius_eq = other._radius == self._radius
        return origin_eq and radius_eq
