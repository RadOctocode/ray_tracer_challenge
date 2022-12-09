from Tuple import Tuple


class Color:
    """
        Color stores a pixel color in an object
    """
    def __init__(self, x, y, z):
        self._red = x
        self._green = y
        self._blue = z
        self._w = 1.0

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    def __add__(self, other):
        new_r = self.red + other.red
        new_g = self.green + other.green
        new_b = self.blue + other.blue

        return Color(new_r, new_g, new_b)

    def __sub__(self, other):
        new_r = self.red - other.red
        new_g = self.green - other.green
        new_b = self.blue - other.blue

        return Color(new_r, new_g, new_b)

    def __mul__(self, other):
        if isinstance(other, Color):
            return Color(
                self.red * other.red,
                self.green * other.green,
                self.blue * other.blue)
        else:
            return Color(
                self.red * other,
                self.green * other,
                self.blue * other)

    def __eq__(self, other):
        red_equals = round(self.red, 5) == round(other.red, 5)
        green_equals = round(self.green, 5) == round(other.green, 5)
        blue_equals = round(self.blue, 5) == round(other.blue, 5)

        return red_equals and green_equals and blue_equals
