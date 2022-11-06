import unittest
from Ray import Ray, position
from Tuple import Tuple, Vector, Point
from Shapes import Sphere
from Intersection import Intersection, Intersections


class RayTest(unittest.TestCase):

    def test_ray_constructor(self):
        origin = Point(1, 2, 3)
        direction = Vector(4, 5, 6)
        test_ray = Ray(origin, direction)
        self.assertEqual(test_ray.origin, origin)
        self.assertEqual(test_ray.direction, direction)

    def test_ray_distance(self):
        origin = Point(2, 3, 4)
        direction = Vector(1, 0, 0)
        test_ray = Ray(origin, direction)
        a = position(test_ray, 0)
        expected_a = Point(2, 3, 4)
        b = position(test_ray, 1)
        expected_b = Point(3, 3, 4)
        c = position(test_ray, -1)
        expected_c = Point(1, 3, 4)
        d = position(test_ray, 2.5)
        expected_d = Point(4.5, 3, 4)

        self.assertEqual(a, expected_a)
        self.assertEqual(b, expected_b)
        self.assertEqual(c, expected_c)
        self.assertEqual(d, expected_d)

    def test_ray_sphere_intersection_hit_2_points(self):
        origin = Point(0, 0, -5)
        direction = Vector(0, 0, 1)
        test_ray = Ray(origin, direction)
        test_sphere = Sphere()
        intersect_test = test_sphere.intersect(test_ray)
        self.assertEqual(intersect_test.count, 2)
        self.assertEqual(intersect_test[0].point, 4.0)
        self.assertEqual(intersect_test[1].point, 6.0)

    def test_ray_intersection_tangent(self):
        origin = Point(0, 1, -5)
        direction = Vector(0, 0, 1)
        test_ray = Ray(origin, direction)
        test_sphere = Sphere()
        intersect_test = test_sphere.intersect(test_ray)
        self.assertEqual(intersect_test.count, 2)
        self.assertEqual(intersect_test[0].point, 5.0)
        self.assertEqual(intersect_test[1].point, 5.0)

    def test_ray_intersection_miss(self):
        origin = Point(0, 2, -5)
        direction = Vector(0, 0, 1)
        test_ray = Ray(origin, direction)
        test_sphere = Sphere()
        intersect_test = test_sphere.intersect(test_ray)
        self.assertEqual(intersect_test.count, 0)

    def test_ray_intersection_inside_sphere(self):
        origin = Point(0, 0, 0)
        direction = Vector(0, 0, 1)
        test_ray = Ray(origin, direction)
        test_sphere = Sphere()
        intersect_test = test_sphere.intersect(test_ray)
        self.assertEqual(intersect_test.count, 2)
        self.assertEqual(intersect_test[0].point, -1.0)
        self.assertEqual(intersect_test[1].point, 1.0)

    def test_ray_intersection_behind_sphere(self):
        origin = Point(0, 0, 5)
        direction = Vector(0, 0, 1)
        test_ray = Ray(origin, direction)
        test_sphere = Sphere()
        intersect_test = test_sphere.intersect(test_ray)
        self.assertEqual(intersect_test.count, 2)
        self.assertEqual(intersect_test[0].point, -6.0)
        self.assertEqual(intersect_test[1].point, -4.0)
