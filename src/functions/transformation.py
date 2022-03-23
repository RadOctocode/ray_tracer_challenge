from Matrix import Matrix
from math import pi, cos, sin

def _turn_to_radians(degree):
    return (degree/180)*pi

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
    sample_matrix = [[1, 0, 0, 0],
        [0, cos(radians), sin(radians)*-1, 0],
        [0, sin(radians), cos(radians), 0],
        [0, 0, 0, 1]]
    return Matrix(sample_matrix)

def rotation_y(radians):
    """
        returns a rotation matrix in the y axis
    """
    sample_matrix = [[cos(radians), 0, sin(radians), 0],
    [0, 1, 0, 0],
    [sin(radians)*-1, 0, cos(radians), 0],
    [0, 0, 0, 1]]
    return Matrix(sample_matrix)

def rotation_z(radians):
    """
        returns the roation matrix in the z axis
    """
    sample_matrix = [[cos(radians), sin(radians)*-1, 0, 0],
        [sin(radians), cos(radians), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]
    return Matrix(sample_matrix)

def shearing(x_a, x_b, y_a, y_b, z_a, z_b):
    """
        returns a shearing matrix
    """
    sample_matrix = [[1, x_a, x_b, 0],
        [y_a, 1, y_b, 0],
        [z_a, z_b, 1, 0],
        [0, 0, 0, 1]]
    return Matrix(sample_matrix)