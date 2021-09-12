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
    
    def at(self, x, y):
        try:
            return self._canvas[y][x]
        except IndexError:
            raise IndexError('index out of bounds!')
    
    def write_pixel(self, x, y, color):
        """
            writes a color to a pixel in a canvas
        """
        try:
            self._canvas[y][x] = color
        except IndexError:
            raise IndexError('index out of bounds!')

    def write_to_PPM(canvas, file_name):
        with open(file_name,'a') as file:
            file.write("P3\n")
            file.write(f"{canvas.width} {canvas.height}\n")
            file.write("255\n")