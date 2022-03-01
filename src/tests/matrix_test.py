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
    
        #the inversion rounds to the 5th digit
    
        #test 1
        a = [[-5, 2, 6, -8],
            [1, -5, 1, 8],
            [7, 7, -6, -7],
            [1, -3, 7, 4]]
        b = [[0.21805, 0.45113, 0.24060, -0.04511],
            [-0.80827, -1.45677, -0.44361, 0.52068],
            [-0.07895, -0.22368, -0.05263, 0.19737],
            [-0.52256, -0.81391, -0.30075, 0.30639]]
        mat_a = Matrix(a)
        mat_b = Matrix(b)
        invert_mat = mat_a.invert()
        for i in range(mat_b.height):
            for j in range(mat_b.width):
                self.assertAlmostEqual(mat_b[(i,j)], invert_mat[(i,j)],5)

        #test 2
        a = [[8, -5, 9, 2],
            [7, 5, 6, 1],
            [-6, 0, 9, 6],
            [-3, 0, -9, -4]]
        b = [[-0.15385, -0.15385, -0.28205, -0.53846],
            [-0.07692, 0.12308, 0.02564, 0.03077],
            [0.35897, 0.35897, 0.43590, 0.92308],
            [-0.69231, -0.69231, -0.76923, -1.92308]]
        mat_a = Matrix(a)
        mat_b = Matrix(b)
        mat_b = Matrix(b)
        invert_mat = mat_a.invert()
        for i in range(mat_b.height):
            for j in range(mat_b.width):
                self.assertAlmostEqual(mat_b[(i,j)], invert_mat[(i,j)],5)
        #test 3
        a = [[9, 3, 0, 9],
            [-5, -2, -6, -3],
            [-4, 9 , 6, 4],
            [-7, 6, 6, 2]]
        b = [[-0.04074, -0.07778, 0.14444, -0.22222],
            [-0.07778, 0.03333, 0.36667, -0.33333],
            [-0.02901, -0.14630, -0.10926, 0.12963],
            [0.17778, 0.06667, -0.26667, 0.33333]]
        mat_a = Matrix(a)
        mat_b = Matrix(b)
        mat_b = Matrix(b)
        invert_mat = mat_a.invert()
        for i in range(mat_b.height):
            for j in range(mat_b.width):
                self.assertAlmostEqual(mat_b[(i,j)], invert_mat[(i,j)],5)

    def test_inversion_multiplication(self):
        a = [[3, -9, 7, 3],
            [3, -8, 2, -9],
            [-4, 4, 4, 1],
            [-6, 5, -1, 1]]
        b = [[8, 2, 2, 2],
            [3, -1, 7, 0],
            [7, 0, 5, 4],
            [6, -2, 0, 5]]
        
        mat_a = Matrix(a)
        mat_b = Matrix(b)
        mat_c = mat_a * mat_b
        undo_matrix =  mat_c * mat_b.invert()
        for i in range(mat_b.height):
            for j in range(mat_b.width):
                self.assertAlmostEqual(mat_a[(i,j)], undo_matrix[(i,j)],5)