from asyncio import TimerHandle
from re import I
import unittest
from Matrix import Matrix
from Tuple import Point
from Tuple import Vector
from functions.transformation import rotation_x, rotation_y, rotation_z, scaling, translation, shearing
from math import pi, sqrt


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
        self.assertEqual(actual, expected)

    def test_scaling_reflection(self):
        """
            multiplying by a negative scaling value
        """
        transform = scaling(-1, 1, 1)
        point = Point(2, 3, 4)
        expected = Point(-2, 3, 4)
        actual = transform * point
        self.assertEqual(expected, actual)

    def test_rotate_around_x(self):
        """
            test the rotate around x function
        """
        point = Point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        full_quarter = rotation_x(pi / 2)
        hq_expected = Point(0, sqrt(2) / 2, sqrt(2) / 2)
        fq_expected = Point(0, 0, 1)
        hq_actual = half_quarter * point
        fq_actual = full_quarter * point

        self.assertAlmostEqual(fq_expected.x, fq_actual.x, 5)
        self.assertAlmostEqual(fq_expected.y, fq_actual.y, 5)
        self.assertAlmostEqual(fq_expected.z, fq_actual.z, 5)

        self.assertAlmostEqual(hq_expected.x, hq_actual.x, 5)
        self.assertAlmostEqual(hq_expected.y, hq_actual.y, 5)
        self.assertAlmostEqual(hq_expected.z, hq_actual.z, 5)

    def test_inverse_rotation_x(self):
        """
            check the inverse of an x rotation rotates in the opposite direction
        """
        point = Point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        inverse = half_quarter.invert()
        hq_expected = Point(0, sqrt(2) / 2, -1 * sqrt(2) / 2)
        hq_actual = inverse * point

        self.assertAlmostEqual(hq_expected.x, hq_actual.x, 5)
        self.assertAlmostEqual(hq_expected.y, hq_actual.y, 5)
        self.assertAlmostEqual(hq_expected.z, hq_actual.z, 5)

    def test_rotate_around_y(self):
        """
            test the rotate around y function
        """
        point = Point(0, 0, 1)
        half_quarter = rotation_y(pi / 4)
        full_quarter = rotation_y(pi / 2)
        hq_expected = Point(sqrt(2) / 2, 0, sqrt(2) / 2)
        fq_expected = Point(1, 0, 0)
        hq_actual = half_quarter * point
        fq_actual = full_quarter * point

        self.assertAlmostEqual(fq_expected.x, fq_actual.x, 5)
        self.assertAlmostEqual(fq_expected.y, fq_actual.y, 5)
        self.assertAlmostEqual(fq_expected.z, fq_actual.z, 5)

        self.assertAlmostEqual(hq_expected.x, hq_actual.x, 5)
        self.assertAlmostEqual(hq_expected.y, hq_actual.y, 5)
        self.assertAlmostEqual(hq_expected.z, hq_actual.z, 5)

    def test_rotate_around_z(self):
        """
            test the rotate around z function
        """
        point = Point(0, 1, 0)
        half_quarter = rotation_z(pi / 4)
        full_quarter = rotation_z(pi / 2)
        hq_expected = Point(-1 * sqrt(2) / 2, sqrt(2) / 2, 0)
        fq_expected = Point(-1, 0, 0)
        hq_actual = half_quarter * point
        fq_actual = full_quarter * point

        self.assertAlmostEqual(fq_expected.x, fq_actual.x, 5)
        self.assertAlmostEqual(fq_expected.y, fq_actual.y, 5)
        self.assertAlmostEqual(fq_expected.z, fq_actual.z, 5)

        self.assertAlmostEqual(hq_expected.x, hq_actual.x, 5)
        self.assertAlmostEqual(hq_expected.y, hq_actual.y, 5)
        self.assertAlmostEqual(hq_expected.z, hq_actual.z, 5)

    def test_shearing_x_in_y(self):
        transform = shearing(1, 0, 0, 0, 0, 0)
        point = Point(2, 3, 4)
        expected = Point(5, 3, 4)
        actual = transform * point

        self.assertEqual(expected, actual)

    def test_shearing_x_in_z(self):
        transform = shearing(0, 1, 0, 0, 0, 0)
        point = Point(2, 3, 4)
        expected = Point(6, 3, 4)
        actual = transform * point

        self.assertEqual(expected, actual)

    def test_shearing_y_in_x(self):
        transform = shearing(0, 0, 1, 0, 0, 0)
        point = Point(2, 3, 4)
        expected = Point(2, 5, 4)
        actual = transform * point

        self.assertEqual(expected, actual)

    def test_shearing_y_in_z(self):
        transform = shearing(0, 0, 0, 1, 0, 0)
        point = Point(2, 3, 4)
        expected = Point(2, 7, 4)
        actual = transform * point

        self.assertEqual(expected, actual)

    def test_shearing_z_in_x(self):
        transform = shearing(0, 0, 0, 0, 1, 0)
        point = Point(2, 3, 4)
        expected = Point(2, 3, 6)
        actual = transform * point

        self.assertEqual(expected, actual)

    def test_shearing_z_in_y(self):
        transform = shearing(0, 0, 0, 0, 0, 1)
        point = Point(2, 3, 4)
        expected = Point(2, 3, 7)
        actual = transform * point

        self.assertEqual(expected, actual)

    def test_chaining_transformations(self):
        transform_A = rotation_x(pi / 2)
        transform_B = scaling(5, 5, 5)
        transform_C = translation(10, 5, 7)
        point = Point(1, 0, 1)
        final_transform = transform_C * transform_B * transform_A
        one_matrix_actual = final_transform * point
        multi_matrix_actual = transform_C * transform_B * transform_A * point
        expected = Point(15, 0, 7)
        self.assertEqual(expected, one_matrix_actual)
        self.assertEqual(expected, multi_matrix_actual)
