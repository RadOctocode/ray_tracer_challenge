from Matrix import Matrix

def translation(x, y, z):
    """
    returns a translation Matrix
    """
    sample_matrix = [[1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]]
    return Matrix(sample_matrix)

def scaling(x, y, z):
    """
        returns a scaling matrix
    """
    sample_matrix = [[x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]]
    return Matrix(sample_matrix)

def rotation_x(radians):
    """
        returns a rotation matrix in the x axis
    """

def rotation_y(radians):
    """
        returns a rotation matrix in the y axis
    """

def shearing(x_a, x_b, y_a, y_b, z_a, z_b):
    """
        returns a shearing matrix
    """