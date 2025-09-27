import unittest
from GeomLib import circle_area, triangle_area

class TestGeomLib(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), 78.53981633974483)
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(TypeError):
            circle_area("string")

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0)
        with self.assertRaises(ValueError):
            triangle_area(1, 1, 3)  # Невозможный треугольник
        with self.assertRaises(TypeError):
            triangle_area(3, 4, "five")  # Неверный тип параметра

if __name__ == '__main__':
    unittest.main()