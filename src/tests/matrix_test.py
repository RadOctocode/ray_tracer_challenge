import unittest
from Matrix import Matrix
from Tuple import Tuple


class MatrixTest(unittest.TestCase):
    """
        test for the 4 by 4 matrix
    """

    def test_matrix_initialization_4_by_4(self):
        """
            test matrix init 4x4
        """
        a = [[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [
            9, 10, 11, 12], [13.5, 14.5, 15.5, 16.5]]
        b = Matrix(a)
        self.assertEqual(b[(0, 0)], 1)
        self.assertEqual(b[(0, 3)], 4)
        self.assertEqual(b[(1, 0)], 5.5)
        self.assertEqual(b[(1, 2)], 7.5)
        self.assertEqual(b[(2, 2)], 11)
        self.assertEqual(b[(3, 0)], 13.5)
        self.assertEqual(b[(3, 2)], 15.5)

    def test_matrix_initialization_2_by_2(self):
        """
            test matrix init 2x2
        """
        a = [[-3, 5], [1, -2]]
        b = Matrix(a)
        self.assertEqual(b[(0, 0)], -3)
        self.assertEqual(b[(0, 1)], 5)
        self.assertEqual(b[(1, 0)], 1)
        self.assertEqual(b[(1, 1)], -2)

    def test_matrix_initialization_3_by_3(self):
        """
            test matrix init 3x3
        """
        a = [[-3, 5, 0], [1, -2, -7], [0, 1, 1]]
        b = Matrix(a)
        self.assertEqual(b[(0, 0)], -3)
        self.assertEqual(b[(2, 2)], 1)
        self.assertEqual(b[(1, 1)], -2)

    def test_matrix_equality(self):
        """
            test matrix equality
        """
        a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
        d = [[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]]

        b = Matrix(a)
        c = Matrix(a)
        e = Matrix(d)
        assert(b == c)
        assert(b != e)

    def test_matrix_multiplication_matrix_to_matrix(self):

        a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
        b = [[-2, 1, 2, 3], [3, 2, 1, -1], [4, 3, 6, 5], [1, 2, 7, 8]]
        c = [[20, 22, 50, 48], [44, 54, 114, 108],
             [40, 58, 110, 102], [16, 26, 46, 42]]

        mat_a = Matrix(a)
        mat_b = Matrix(b)
        expected = Matrix(c)
        actual = mat_a * mat_b

        self.assertEqual(expected, actual)

