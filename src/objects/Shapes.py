from Tuple import Point, dot_product
from math import sqrt


class Sphere:
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
        sphere_to_ray = ray.origin - self.origin
        a = dot_product(ray.direction, ray.direction)
        b = 2 * dot_product(ray.direction, sphere_to_ray)
        c = dot_product(sphere_to_ray, sphere_to_ray) - 1

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []

        neg_b = b * -1
        t1 = (neg_b - sqrt(discriminant)) / (2 * a)
        t2 = (neg_b + sqrt(discriminant)) / (2 * a)

        return [t1, t2]
