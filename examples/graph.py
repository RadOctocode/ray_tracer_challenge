from Tuple import Tuple, Vector, Point
from Canvas import Canvas
from Color import Color
from objects.Tuple import normalize


class Projectile:
    def __init__(self, position, velocity):
        """
            position is a point
            velocity is a vector
        """
        self._position = position
        self._velocity = velocity

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity


class Environment:
    def __init__(self, gravity, wind):
        """
            gravity is a vector
            wind is also a vector
        """
        self._gravity = gravity
        self._wind = wind

    @property
    def gravity(self):
        return self._gravity

    @property
    def wind(self):
        return self._wind


def tick(environment, projectile):
    """
        move time forward once
        return a new projectile
    """
    new_position = projectile.position + projectile.velocity
    new_velocity = projectile.velocity + environment.gravity + environment.wind
    return Projectile(new_position, new_velocity)


if __name__ == "__main__":
    print("Shooting Projectile\n")

    start = Point(0,1,0)
    velocity = normalize(Vector(1.0, 1.8, 0)) * 11.25
    p2 = Projectile(start,velocity)
    gravity = Vector(0.0, -0.1, 0.0)
    wind = Vector(-0.01, 0.0, 0.0)
    e = Environment(gravity, wind)

    c = Canvas(900, 550)
    red = Color(1.0, 0.0, 0.0)
    green = Color (0.0,1.0,0.0)
    c.write_pixel(10,10,green)
    while p2.position.y > 0:
        p2 = tick(e, p2)
        c.write_pixel(round(p2.position.x), round(p2.position.y), red)
    c.write_to_PPM("graph.ppm")
