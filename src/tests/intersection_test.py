import unittest
from Intersection import Intersection, Intersections
from Shapes import Sphere
from Ray import Ray
from Tuple import Point, Vector


class RayTest(unittest.TestCase):

    def test_interesction_construtor(self):
        s = Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(i.point, 3.5)
        self.assertEqual(i.object, s)

    def test_aggregating_intersections(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections([i1, i2])
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].point, 1)
        self.assertEqual(xs[1].point, 2)

    def test_sets_object_on_intersection(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(xs.count, 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_determine_hit_both_intersections_positive(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = Intersections([i1, i2])
        i = xs.hit()
        self.assertEqual(i, i1)

    def test_determine_hit_some_intersections_negative(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = Intersections([i2, i1])
        i = xs.hit()
        self.assertEqual(i, i2)

    def test_determine_hit_both_intersection_negative(self):
        s = Sphere()
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = Intersections([i2, i1])
        i = xs.hit()
        self.assertEqual(i, None)

    def test_determine_hit_always_lowest_negative_number(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = Intersections([i1, i2, i3, i4])
        i = xs.hit()
        self.assertEqual(i, i4)
