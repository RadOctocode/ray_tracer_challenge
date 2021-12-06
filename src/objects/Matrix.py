from Tuple import Tuple


class Matrix:
    def __init__(self, matrix):
        """
            assuming matrix is a list of lists
        """
        self._matrix = matrix
        self._height = len(matrix)
        if self._height != 0:
            self._width = len(matrix[0])
        else:
            self._width = 0

    @property
    def matrix(self):
        return self._matrix

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def __getitem__(self, arg):
        """
            assuming arg is a pair of values
        """
        arg0, arg1 = arg
        return self.matrix[arg0][arg1]

    def __eq__(self, other):
        if other.width != self.width or other.height != self.height:
            return False
        else:
            for i in range(len(self.matrix)):
                if other.matrix[i] != self.matrix[i]:
                    return False
        return True

    def __mul__(self, other):
        """make sure the number of cols in matrix 1 == rows in matrix 2"""
        if isinstance(other, Matrix):
            if self._width == other._height:
                final_matrix = [[0 for x in range(other.width)] for y in range(self.height)] 
                for col in range(self.height):
                    for row in range(other.width):
                        current_result = self._multiply_helper(other, col, other.height, row)
                        final_matrix[row][col] = current_result
                return Matrix(final_matrix)
        elif isinstance(other, Tuple):
            if self._width == 4:
                tuple_values = [0,0,0,0]
                for i in range(self._width):
                    current_row = self.matrix[i]
                    tuple_values[i] = current_row[0]*other.x + current_row[1]*other.y + current_row[2]*other.z + current_row[3]*other.w
                return Tuple(tuple_values[0], tuple_values[1], tuple_values[2], tuple_values[3])
                    
        raise Exception("make sure the # of cols in matrix A equal the # of rows in matrix B")
    
    def _multiply_helper(self, other, col, height, row):
        """
            multiplies the other col by the self row  
            then adds it together
        """
        return_value = 0
        self_row = self.matrix[row]
        for i in range(height):
            return_value += self_row[i] * other.matrix[i][col]

        return return_value