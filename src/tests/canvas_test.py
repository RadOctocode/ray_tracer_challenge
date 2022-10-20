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
                print(
                    f"{a._canvas[i][j].red},{a._canvas[i][j].green},{a._canvas[i][j].blue},{a._canvas[i][j]._w}")
                self.assertEqual(a._canvas[i][j], Color(0.0, 0.0, 0.0))

    def test_writing_pixel_to_canvas(self):
        red = Color(1.0, 0.0, 0.0)
        a = Canvas(10, 20)
        a.write_pixel(2, 3, red)

        new_color = a.at(2, 3)
        self.assertEqual(new_color, red)

    def test_writing_to_ppm(self):
        c1 = Color(1.5, 0.0, 0.0)
        c2 = Color(0.0, 0.5, 0.0)
        c3 = Color(-0.5, 0.0, 1.0)
        a = Canvas(5, 3)

        a.write_pixel(0, 0, c1)
        a.write_pixel(2, 1, c2)
        a.write_pixel(4, 2, c3)

        a.write_to_PPM("test.ppm")
        with open("test.ppm", 'r') as file:
            lines = file.readlines()

            # test to see if the heading is correct
            self.assertEqual(lines[0], "P3\n")
            self.assertEqual(lines[1], "5 3\n")
            self.assertEqual(lines[2], "255\n")

            # figure out if the contents are good
            self.assertEqual(lines[3], "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n")
            self.assertEqual(lines[4], "0 0 0 0 0 0 0 127 0 0 0 0 0 0 0\n")
            self.assertEqual(lines[5], "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n")

            # make sure the file ends with a new line
            self.assertEqual(lines[6], "\n")

    def test_splitting_a_ppm(self):
        c1 = Color(1, 0.8, 0.6)
        a = Canvas(10, 2, c1)
        a.write_to_PPM("test2.ppm")
        with open("test2.ppm", 'r') as file:
            lines = file.readlines()

            # make sure that the lines

            self.assertEqual(
                lines[3],
                "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n")
            self.assertEqual(
                lines[4],
                "153 255 204 153 255 204 153 255 204 153 255 204 153\n")
            self.assertEqual(
                lines[5],
                "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n")
            self.assertEqual(
                lines[6],
                "153 255 204 153 255 204 153 255 204 153 255 204 153\n")
