import unittest
from GeomLib import Circle, Triangle

class TestGeomLib(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(TypeError):
            Circle("string")

    def test_triangle_area_and_rectangular_check(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
        self.assertTrue(triangle.is_right_angled())
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # Недопустимый треугольник
        with self.assertRaises(TypeError):
            Triangle(3, 4, "five")  # Некорректный тип аргумента

if __name__ == '__main__':
    unittest.main()