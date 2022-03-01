from Tuple import Tuple

def tuple_id_matrix():
    id = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    return Matrix(id)


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
            print("mismatch width/ height")
            return False
        else:
            for i in range(len(self.matrix)):
                if other.matrix[i] != self.matrix[i]:
                    print("mismatch object")
                    return False
        return True


    def __mul__(self, other):
        """make sure the number of cols in matrix 1 == rows in matrix 2"""
        if isinstance(other, Matrix):
            if self._width == other._height:
                final_matrix = [
                    [0 for x in range(other.width)] for y in range(self.height)]
                for col in range(self.height):
                    for row in range(other.width):
                        current_result = self._multiply_helper(
                            other, col, other.height, row)
                        final_matrix[row][col] = current_result
                return Matrix(final_matrix)
        elif isinstance(other, Tuple):
            if self._width == 4:
                tuple_values = [0, 0, 0, 0]
                for i in range(self._width):
                    current_row = self.matrix[i]
                    tuple_values[i] = current_row[0] * other.x + current_row[1] * \
                        other.y + current_row[2] * \
                        other.z + current_row[3] * other.w
                return Tuple(tuple_values[0], tuple_values[1], tuple_values[2], tuple_values[3])

        raise Exception(
            "make sure the # of cols in matrix A equal the # of rows in matrix B")

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
    
    def get_identity_matrix(self):
        """
            get the identity matrix
            returns identity matrix
        """
        if self.width == self.height:
            id_matrix = [[0 for x in range(self.width)]for y in range(self.height)]
            for i in range(self.width):
                id_matrix[i][i] = 1
            return Matrix(id_matrix)
                
        raise Exception("the identity matrix must be square")        

    def print_matrix(self):
        """
            matrix pretty print
        """
        for i in range(self.height):
            print_str = ""
            for j in range(self.width):
                    print_str = print_str+"|"+str(self.matrix[i][j])+"|"
            print(print_str)
            print("\n")
    
    def transpose(self):
        """
            rotate the matrix
            return the transpose of the matrix
        """
        new_matrix = [[0 for x in range(self.height)]for y in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                    new_matrix[j][i] = self.matrix[i][j]

        return Matrix(new_matrix)

    def invert(self):
        """
            find the inverse of a matrix
            round to 5 decimal places
            return the inverse of a matrix
        """
        current_determinant = self.find_determinant()
        if current_determinant == 0:
            raise Exception("the matrix is not invertible")
        else:
            new_matrix = [[0 for x in range(self.width)]for y in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    current_cofactor = self.find_cofactor(i, j)
                    new_matrix[j][i] = current_cofactor/current_determinant
            return Matrix(new_matrix)


    def find_determinant(self):
        """
            find the determinant of the 2x2 matrix
            returns determinant
        """
        if self.height == 2 and self.width == 2:
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
        else:
            determinant = 0
            for j in range(self.width):
                determinant += self.matrix[0][j] * self.find_cofactor(0, j)
            return determinant

    def find_submatrix(self, row, col):
        """
            find the submatrix by removing the row and col indicated
            returns new submatrix
        """
        new_width = self.width - 1
        new_height = self.height - 1
        if new_width >= 0 and new_height >= 0:
            if row < self.height and col < self.width:
                new_matrix = [[0 for x in range(new_width)]for y in range(new_height)]
                new_col_index = 0
                new_row_index = 0
                for i in range(self.height):
                    new_row_index = 0
                    if i != row:
                        for j in range(self.width):
                            if j != col:
                                new_matrix[new_col_index][new_row_index] = self.matrix[i][j]
                                new_row_index += 1
                        new_col_index += 1
                return Matrix(new_matrix)

            else:
                raise Exception("you're removing a row/ col that doesn't exist")

    def find_minor(self, row, col):
        """
            find the minor of a matrix
            returns the minor
        """
        new_submatrix = self.find_submatrix(row, col)
        return new_submatrix.find_determinant()
    
    def find_cofactor(self, row, col):
        """
            find the cofactor of a 3 by 3 matrix
        """
        multiply = 1
        if (row + col)%2 == 1:
            multiply = -1
        return self.find_minor(row, col) * multiply

#backend systems developer
#features delivery
#REST api graphql and database design