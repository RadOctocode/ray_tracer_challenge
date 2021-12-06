import unittest
from math import sqrt
from Tuple import Tuple, Vector, Point
from Tuple import cross_product, dot_product, magnitude, normalize

class TupleTest(unittest.TestCase):
    
    """
        tests for the tuple class
    """

    def test_create_tuple_vector(self):
        """
            this should create vector
        """
        expected_x = 0.3
        expected_y = 1.1
        expected_z = 2.2
        expected_w = 0.0
        actual = Tuple(0.3, 1.1, 2.2, 0.0)

        self.assertEqual(expected_x, actual.x)
        self.assertEqual(expected_y, actual.y)
        self.assertEqual(expected_z, actual.z)
        self.assertEqual(expected_w, actual.w)
        self.assertTrue(actual.is_vector())
    
    def test_create_tuple_point(self):

        expected_x = 0.3
        expected_y = 1.1
        expected_z = 2.2
        expected_w = 1.0
        actual = Tuple(0.3, 1.1, 2.2, 1.0)
    
        self.assertEqual(expected_x, actual.x)
        self.assertEqual(expected_y, actual.y)
        self.assertEqual(expected_z, actual.z)
        self.assertEqual(expected_w, actual.w)
        self.assertTrue(actual.is_point())

    def test_create_vector(self):
        """
            this should create vector with vector constructor
        """
        expected_x = 0.3
        expected_y = 1.1
        expected_z = 2.2
        expected_w = 0.0
        actual = Vector(0.3, 1.1, 2.2)

        self.assertEqual(expected_x, actual.x)
        self.assertEqual(expected_y, actual.y)
        self.assertEqual(expected_z, actual.z)
        self.assertEqual(expected_w, actual.w)
        self.assertTrue(actual.is_vector())

    def test_create_point(self):
        """
            this should create point with point constructor
        """
        expected_x = 0.3
        expected_y = 1.1
        expected_z = 2.2
        expected_w = 1.0
        actual = Point(0.3, 1.1, 2.2)

        self.assertEqual(expected_x, actual.x)
        self.assertEqual(expected_y, actual.y)
        self.assertEqual(expected_z, actual.z)
        self.assertEqual(expected_w, actual.w)
        self.assertTrue(actual.is_point())

    def test_tuple_equals_operation(self):
        a = Tuple(3.0, -2.0, 5.0, 1.0)
        b = Tuple(3.0, -2.0, 5.0, 1.0)
        self.assertEqual(a, b)
    
    def test_tuple_add_operation(self):
        a = Tuple(3.0, -2.0, 5.0, 1.0)
        b = Tuple(-2.0, 3.0, 1.0, 0.0)

        expected = Tuple(1.0, 1.0, 6.0, 1.0)
        actual = a + b
        self.assertEqual(actual, expected)

    def test_subtract_operation_point_from_point(self):
        a = Point (3.0, 2.0, 1.0)
        b = Point (5.0, 6.0, 7.0)
        expected = Vector(-2.0, -4.0, -6.0)
        actual = a - b

        self.assertEqual(actual, expected)
        self.assertTrue(actual.is_vector())


    def test_subtract_operation_point_from_point(self):
        a = Point (3.0, 2.0, 1.0)
        b = Point (5.0, 6.0, 7.0)
        expected = Vector(-2.0, -4.0, -6.0)
        actual = a - b

        self.assertEqual(actual, expected)
        self.assertTrue(actual.is_vector())
    
    def test_subtract_point_from_vector(self):
        a = Point(3.0, 2.0, 1.0)    
        b = Vector(5.0, 6.0, 7.0)
        expected = Point(-2.0, -4.0, -6.0)
        actual = a - b

        self.assertEqual(actual, expected)
        self.assertTrue(actual.is_point())
    
    def test_subtract_vector_from_vector(self):
        a = Vector(3.0, 2.0, 1.0)    
        b = Vector(5.0, 6.0, 7.0)
        expected = Vector(-2.0, -4.0, -6.0)
        actual = a - b

        self.assertEqual(actual, expected)
        self.assertTrue(actual.is_vector())

    def test_subtract_vector_from_zero_vector(self):
        a = Vector(0.0, 0.0, 0.0)
        b = Vector(5.0, -6.0, -7.0)
        expected = Vector(-5.0, 6.0, 7.0)
        actual = a - b

        self.assertEqual(actual, expected)
        self.assertTrue(actual.is_vector())

    def test_negating_tuple(self):
        a = Tuple(1.0, -2.0, 3.0, -4.0)
        expected = Tuple(-1.0, 2.0, -3.0, 4.0)
        actual = -a

        self.assertEqual(expected, actual)
    
    def test_multiplication_tuple(self):
        a = Tuple(1.0, -2.0, 3.0, -4.0)
        a_expected = Tuple(3.5, -7.0, 10.5, -14.0)
        a_actual = a * 3.5

        self.assertEqual(a_actual, a_expected)
    
        a = Tuple(1.0, -2.0, 3.0, -4.0)
        a_expected = Tuple(0.5, -1.0, 1.5, -2)
        a_actual = a * 0.5

        self.assertEqual(a_actual, a_expected)
    
    def test_division_tuple(self):
        a = Tuple(1.0, -2.0, 3.0, -4.0)
        expected = Tuple(0.5, -1.0, 1.5, -2)
        actual = a/2

        self.assertEqual(expected, actual)

    def test_magnitude_for_vector(self):
        a = Vector(1.0, 0.0, 0.0)
        b = Vector(0.0, 1.0, 0.0)
        c = Vector(0.0, 0.0, 1.0)

        self.assertEqual(magnitude(a), 1.0)
        self.assertEqual(magnitude(b), 1.0)
        self.assertEqual(magnitude(c), 1.0)

        d = Vector(1.0, 2.0, 3.0)
        e = Vector(-1.0, -2.0, -3.0)

        self.assertEqual(magnitude(d), sqrt(14.0))
        self.assertEqual(magnitude(e), sqrt(14.0))

    def test_normalize_for_vector(self):
        a = Vector(4.0, 0.0, 0.0)
        expected_a = Vector(1.0, 0.0, 0.0)
        actual_a = normalize(a)

        self.assertEqual(expected_a, actual_a)

        b = Vector(1.0, 2.0, 3.0)
        expected_b = Vector(1.0/sqrt(14.0), 2.0/sqrt(14.0), 3.0/sqrt(14.0))
        actual_b = normalize(b)
        self.assertEqual(expected_b, actual_b)
    
    def test_magnitide_of_normalized_vector(self):
        a = Vector(1.0, 2.0, 3.0)
        expected = 1.0
        normal_a = normalize(a)
        actual = magnitude(normal_a)

        self.assertEqual(expected, actual)
    
    def test_dot_product(self):
        a = Vector(1.0, 2.0, 3.0)
        expected = 1.0
        normal_a = normalize(a)
        actual = magnitude(normal_a)

        self.assertEqual(expected, actual)
    
    def test_dot_product(self):
        a = Vector(1.0, 2.0, 3.0)
        b = Vector(2.0, 3.0, 4.0)

        expected = 20.0
        actual = dot_product(a, b)
        self.assertEqual(expected, actual)

    def test_cross_product(self):
        a = Vector(1.0, 2.0, 3.0)
        b = Vector(2.0, 3.0, 4.0)

        actual_c = cross_product(a, b)
        actual_d = cross_product(b, a)

        expected_c = Vector(-1.0, 2.0, -1.0)
        expected_d = Vector(1.0, -2.0, 1.0)

        self.assertEqual(expected_d, actual_d)
        self.assertEqual(expected_c, actual_c)
