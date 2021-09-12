import unittest
from Canvas import Canvas
from Color import Color

class CanvasTest(unittest.TestCase):
    """
        tests for the canvas object
    """

    def test_creating_canvas(self):
        a = Canvas(10, 20)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 20)
        for i in range(a.height):
            for j in range(a.width):
                print(f"{a._canvas[i][j].red},{a._canvas[i][j].green},{a._canvas[i][j].blue},{a._canvas[i][j]._w}")
                self.assertEqual(a._canvas[i][j], Color(0.0, 0.0, 0.0))
    
    def test_writing_pixel_to_canvas(self):
        red = Color(1.0, 0.0, 0.0)
        a = Canvas(10, 20)
        a.write_pixel(2, 3, red)

        new_color = a.at(2, 3)
        self.assertEqual(new_color, red)
    
    def test_writing_to_ppm(self):
        a = Canvas(10, 20)

    
