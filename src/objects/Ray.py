from Tuple import Tuple, Vector, Point


def position(ray, distance):
    return ray.origin + ray.direction * distance


class Ray:
    def __init__(self, origin, direction):
        self._origin = origin
        self._direction = direction

    @property
    def origin(self):
        return self._origin

    @property
    def direction(self):
        return self._direction
