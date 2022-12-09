
from cmath import inf


class Intersection:
    """
        The Intersection class holds a point and an object
        the point is the point of intersection
        the object is the object being intersected

    """

    def __init__(self, point, object):
        self._int_point = point
        self._object = object

    def __lt__(self, other):
        return ((self._int_point) < (other._int_point))

    def __gt__(self, other):
        return ((self._int_point) > (other._int_point))

    def __le__(self, other):
        return ((self._int_point) <= (other._int_point))

    def __ge__(self, other):
        return ((self._int_point) >= (other._int_point))

    def __eq__(self, other):
        return ((self._int_point) == (other._int_point))

    @property
    def point(self):
        return self._int_point

    @property
    def object(self):
        return self._object


class Intersections:
    """
        The Intersections class has an array
        the array holds an array of intersections
    """

    def __init__(self, array):
        self._array = sorted(array)

    def __getitem__(self, index):
        return self._array[index]

    @property
    def count(self):
        return len(self._array)

    def add(self, intersection):
        """
            adds an intersection to the arrayin a sorted way
            returns index added
        """
        for i in range(len(self._array)):
            if self._array[i] >= intersection:
                self._array.insert(i, intersection)
                return i

        self._array.insert(len(self._array) - 1, intersection)

    def hit(self):
        """
            returns the lowest non negative intersection
            if there is no non-negative intersection
        """
        highest_value = float(inf)
        highest_intersection_index = 0
        for i in range(len(self._array)):
            current_intersection = self._array[i]
            if current_intersection.point < highest_value and current_intersection.point > 0:
                highest_value = current_intersection.point
                highest_intersection_index = i
        if highest_value == float(inf):
            return None
        return self._array[highest_intersection_index]
