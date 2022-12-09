from Tuple import Tuple, Vector, Point


def position(ray, distance):
    """
        takes a ray and a distance
        returns a specific position
    """
    return ray.origin + ray.direction * distance


class Ray:
    """
        The Ray class represents rays 
        to create a ray you need an origin and a direction
    """
    def __init__(self, origin, direction):
        self._origin = origin
        self._direction = direction

    @property
    def origin(self):
        return self._origin

    @property
    def direction(self):
        return self._direction
    
    def transform(self, transformation):
        point_list = self.origin.return_as_list()
        direction_list = self.direction.return_as_list()
        ray_matrix = [point_list,direction_list]

        transformed_matrix = transformation * ray_matrix
        transformed_point_list = transformed_matrix.matrix[0]
        transformed_direction_list = transformed_matrix.matrix[1]
        ret_origin = Point(transformed_point_list[0],
        transformed_point_list[1],
        transformed_point_list[2])
        ret_direction = Vector(transformed_direction_list[0],
        transformed_direction_list[1],
        transformed_direction_list[2])
        return Ray(ret_origin, ret_direction)
