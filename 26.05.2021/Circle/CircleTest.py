from Circle import Circle
import unittest
from unittest.mock import Mock
from unittest.mock import patch


class TestValidInputs(unittest.TestCase):
    def setUp(self):
        self.c = Circle(2)

    def test_area(self):
        self.assertEqual(self.c.area(), 12.566370614359172)
        self.assertNotEqual(self.c.area(), 1.566370614359172)
        c = Circle(3)
        self.assertEqual(c.area(), 28.274333882308138)

    def test_area_mock(self):
        area = Mock(return_value=12.566370614359172)
        self.assertEqual(area(), 12.566370614359172)


if __name__ == "main":
    unittest.main()
