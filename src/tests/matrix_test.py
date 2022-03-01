import unittest
from Matrix import Matrix
from Matrix import tuple_id_matrix
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

    def test_matrix_multiplication_matrix_to_tuple(self):

        a = [[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]]
        b = Tuple(1, 2, 3, 1)
        mat_a = Matrix(a)
        expected = Tuple(18, 24, 33, 1)

        actual = mat_a * b
        self.assertEqual(expected, actual)

    def test_identity_matrix_test_matrix(self):
        a = [[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]]
        id = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        mat_a = Matrix(a)
        expected = Matrix(id)

        actual_id_a = mat_a.get_identity_matrix()
        self.assertEqual(expected, actual_id_a)

        product_a = mat_a * actual_id_a
        self.assertEqual(product_a, mat_a)
    
        b = Tuple(1, 2, 3, 1)
        actual_id_b = tuple_id_matrix()
        self.assertEqual(expected, actual_id_b)
    
        product_b = actual_id_b * b
        self.assertEqual(product_b, b)
    
    def test_matrix_transpose_square_matrix(self):
        a = [[0, 9, 3, 0],
            [9, 8, 0, 8],
            [1, 8, 5, 3],
            [0, 0, 5, 8]]

        b = [[0, 9, 1, 0],
             [9, 8, 8, 0], 
             [3, 0, 5, 5], 
             [0, 8, 3, 8]]

        mat_a = Matrix(a)
        mat_b = Matrix(b)
        trans_a = mat_a.transpose()
 
        self.assertEqual(trans_a,mat_b)

    def test_matrix_transpose_rectangle_v_matrix(self):
        a = [[1, 2],
            [3, 4],
            [5, 6]]

        b = [[1, 3, 5],
             [2, 4, 6]]

        mat_a = Matrix(a)
        mat_b = Matrix(b)
        trans_a = mat_a.transpose()

 
        self.assertEqual(trans_a,mat_b)
    
    def test_matrix_transpose_rectangle_h_matrix(self):        
        a = [[1, 3, 5],
             [2, 4, 6]]

        b = [[1, 2],
            [3, 4],
            [5, 6]]

        mat_a = Matrix(a)
        mat_b = Matrix(b)
        trans_a = mat_a.transpose()
 
        self.assertEqual(trans_a,mat_b)

    def test_matrix_determinant_2_by_2(self):
        """
            find the determinant of a 2 by 2 matrix
        """
        a = [[1,5],
            [-3,2]]
        mat_a = Matrix(a)
        a_determinant = mat_a.find_determinant()

        self.assertEqual(a_determinant, 17)
    
    def test_matrix_submatrix_3_by_3(self):
        """
            find the submatrix of a 3 by 3 matrix
        """
        a = [[1, 5, 0],
            [-3, 2, 7],
            [0, 6, -3]]
        b = [[-3, 2],
            [0, 6]]
        mat_a = Matrix(a)
        mat_b = Matrix(b)
        sub_mat_a = mat_a.find_submatrix(0,2)

        self.assertEqual(sub_mat_a, mat_b)

    def test_matrix_submatrix_4_by_4(self):
        """
            find the submatrix of a 3 by 3 matrix
        """
        a = [[-6, 1, 1, 6],
            [-8, 5, 8, 6],
            [-1, 0, 8, 2],
            [-7, 1, -1, 1]]
        b = [[-6, 1, 6],
            [-8, 8, 6],
            [-7, -1, 1]]
        mat_a = Matrix(a)
        mat_b = Matrix(b)
        sub_mat_a = mat_a.find_submatrix(2, 1)

        self.assertEqual(sub_mat_a, mat_b)
    
    def test_matrix_minor_3_by_3(self):
        a = [[3, 5, 0],
            [2, -1, -7],
            [6, -1, 5]]
        mat_a = Matrix(a)
        minor_a = mat_a.find_minor(1, 0)
        self.assertEqual(minor_a, 25)

    def test_matrix_find_cofactor_3_by_3(self):
        a = [[3, 5, 0],
            [2, -1, -7],
            [6, -1, 5]]
        mat_a = Matrix(a)
        expected_1 = mat_a.find_minor(0, 0)
        expected_2 = mat_a.find_minor(1, 0)
        self.assertEqual(expected_1, -12)
        self.assertEqual(expected_1, mat_a.find_cofactor(0,0))
        self.assertEqual(expected_2, 25)
        self.assertEqual(expected_2 * -1, mat_a.find_cofactor(1,0))
    
    def test_matrix_determinant_3_by_3(self):
        a = [[1, 2, 6],
            [-5, 8, -4],
            [2, 6, 4]]
        mat_a = Matrix(a)
        self.assertEqual(56, mat_a.find_cofactor(0,0))
        self.assertEqual(12, mat_a.find_cofactor(0,1))
        self.assertEqual(-46, mat_a.find_cofactor(0,2))
        self.assertEqual(-196, mat_a.find_determinant())
    
    def test_matrix_determinant_4_by_4(self):
        a = [[-2, -8, 3, 5],
            [-3, 1, 7, 3],
            [1, 2, -9, 6],
            [-6, 7, 7, -9]]
        mat_a = Matrix(a)
        self.assertEqual(690, mat_a.find_cofactor(0,0))
        self.assertEqual(447, mat_a.find_cofactor(0,1))
        self.assertEqual(210, mat_a.find_cofactor(0,2))
        self.assertEqual(51, mat_a.find_cofactor(0,3))
        self.assertEqual(-4071, mat_a.find_determinant())
    
    def test_matrix_invertibility(self):
        a = [[6, 4, 4, 4],
            [5, 5, 7, 6],
            [4, -9, 3, -7],
            [9, 1, 7, -6]]
        mat_a = Matrix(a)
        self.assertEqual(-2120, mat_a.find_determinant())

        b = [[-4, 2, -2, -3],
            [9, 6, 2, 6],
            [0, -5, 1, -5],
            [0, 0, 0 , 0]]
        mat_b = Matrix(b)
        self.assertEqual(0, mat_b.find_determinant())

    def test_matrix_inversion(self):
        a = [[-5, 2, 6, -8],
            [1, -5, 1, 8],
            [7, 7, -6, -7],
            [1, -3, 7, 4]]
        mat_a = Matrix(a)