from Color import Color
from math import floor

def _clamp_canvas_value(value):
    #clamp anything over 1 to 1 and under 0 to 0
    if value > 1.0:
        return 1.0
    elif value < 0.0:
        return 0.0
    else:
        return value

class Canvas():
    def __init__(self, width, height, color=Color(0.0,0.0,0.0)):
        self._height = height
        self._width = width
        self._canvas = [[color for j in range(width)]for i in range(height)]

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

    def write_to_PPM(self, file_name):
        with open(file_name,'a') as file:
            file.write("P3\n")
            file.write(f"{self.width} {self.height}\n")
            file.write("255\n")
            for i in range(self.height):
                current_line = ""

                for j in range(self.width):
                    # for each pixel
                    canvas_red = _clamp_canvas_value(self._canvas[i][j].red) * 255.0
                    canvas_green = _clamp_canvas_value(self._canvas[i][j].green) * 255.0
                    canvas_blue = _clamp_canvas_value(self._canvas[i][j].blue) * 255.0

                    if len(current_line) + len(str(floor(canvas_red))) + 1 <= 70:
                        current_line = current_line + str(floor(canvas_red)) + " "
                    else:
                        current_line = current_line.strip()
                        current_line = current_line + "\n"
                        file.write(current_line)
                        current_line = str(floor(canvas_red)) + " "

                    if len(current_line) + len(str(floor(canvas_green))) + 1 <= 70:
                        current_line = current_line + str(floor(canvas_green)) + " "
                    else:
                        current_line = current_line.strip()
                        current_line = current_line + "\n"
                        file.write(current_line)
                        current_line = str(floor(canvas_green)) + " "

                    if len(current_line) + len(str(floor(canvas_blue))) + 1 <= 70:
                        current_line = current_line + str(floor(canvas_blue)) + " "
                    else:
                        current_line = current_line.strip()
                        current_line = current_line + "\n"
                        file.write(current_line)
                        current_line = str(floor(canvas_blue)) + " "

                current_line = current_line.strip()
                current_line = current_line + "\n"
                file.write(current_line)
            file.write("\n")