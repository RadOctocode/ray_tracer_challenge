import unittest
from Color import Color

class ColorTest(unittest.TestCase):
    def test_color_object(self):
        a = Color(-0.5, 0.4, 1.7)
        self.assertEqual(a.red, -0.5)
        self.assertEqual(a.green, 0.4)
        self.assertEqual(a.blue, 1.7)

    def test_adding_colors(self):
        a = Color(0.9, 0.6, 0.75)
        b = Color(0.7, 0.1, 0.25)
        expected = Color(1.6, 0.7, 1.0)
        actual = a + b
        self.assertEqual(expected, actual)

    def test_subtract_colors(self):
        a = Color(0.9, 0.6, 0.75)
        b = Color(0.7, 0.1, 0.25)
        expected = Color(0.2, 0.5, 0.5)
        actual = a - b
        self.assertEqual(expected, actual)

    def test_multiply_by_scalar(self):
        a = Color(0.2, 0.3, 0.4)
        expected = Color(0.4, 0.6, 0.8)
        actual = a * 2
        self.assertEqual(expected, actual)

    def test_test_multiply_by_color(self):
        a = Color(1.0, 0.2, 0.4)
        b = Color(0.9, 1.0, 0.1)
        expected = Color(0.9, 0.2, 0.04)
        actual = a * b
        self.assertEqual(expected, actual)
