from Color import Color

class Canvas():
    def __init__(self, width, height):
        self._height = height
        self._width = width
        self._canvas = [[Color(0.0, 0.0, 0.0) for j in range(width)]for i in range(height)]

    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width