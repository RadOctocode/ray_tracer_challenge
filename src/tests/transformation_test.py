from asyncio import TimerHandle
import unittest
from Matrix import Matrix
from Tuple import Point
from Tuple import Vector
from functions.transformation import scaling, translation
from transformation import *

class TransformationTest(unittest.TestCase):
    """
        test the transformations
    """
    def test_multiply_translation(self):
        """
            multiply by a point
        """
        transform = translation(5, -3, 2)
        point = Point(-3, 4, 5)
        expected = Point(2, 1, 7)
        actual = transform * point

        self.assertEqual(expected, actual)
    
    def test_multiply_inverse_translation(self):
        """
            multiply point by inverse of translation
        """
        transform = translation(5, -3, 2)
        inverse = transform.invert()
        point = Point(-3, 4, 5)
        expected = Point(-8, 7, 3)
        actual = inverse * point
        self.assertEqual(expected, actual)

    def test_multiply_vector_translation(self):
        """
            multiply by a vector does nothing
        """
        transform = translation(5, -3, 2)
        transform.print_matrix()
        v = Vector(-3, 4, 5)
        actual = transform * v
        self.assertEqual(v, actual)
    
    def test_scaling_translation_point(self):
        """
            multiplay a scaling transformation by a point
        """
        transform = scaling(2, 3, 4)
        point = Point(-4, 6, 8)
        expected = Point(-8, 18, 32)
        actual = transform * point
        self.assertEqual(actual, expected)

    def test_scaling_vector(self):
        """
            multiply by vector 
            unlike ranslation this should effect vectors
        """
        transform = scaling(2, 3, 4)
        vector = Vector(-4, 6, 8)
        expected = Vector(-8, 18, 32)
        actual = transform * vector
        self.assertEqual(actual, expected)
    
    def test_scaling_inverse(self):
        transform = scaling(2, 3, 4)
        inverse = transform.invert()
        vector = Vector(-4, 6, 8)
        expected = Vector(-2, 2, 2)
        actual = inverse * vector
        self.assertEqual(actual,expected)
    
    def test_scaling_reflection(self):
        """
            multiplying by a negative scaling value 
        """
        transform = scaling(-1, 1, 1)
        point = Point(2, 3 ,4)
        expected = Point(-2, 3, 4)
        actual = transform * point