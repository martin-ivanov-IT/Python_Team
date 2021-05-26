from Parallelepiped import Parallelepiped
import unittest
from unittest.mock import patch


class TestValidInputs(unittest.TestCase):
    def setUp(self):
        self.par = Parallelepiped(2, 3, 4)

    def demo_area(self):
        return self.width * self.lenght

    @patch('Parallelepiped.Parallelepiped.area', autospec=True, side_effect=demo_area)
    def test_dis(self, area):
        self.assertEqual(self.par.volume(), 24)


if __name__ == "main":
    unittest.main()
