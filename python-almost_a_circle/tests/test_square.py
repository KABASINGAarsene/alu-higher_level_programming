#!/usr/bin/python3


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_initialization(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 99)

    def test_update_args(self):
        s = Square(5)
        s.update(89, 7, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=8, x=2, y=3)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(s.to_dictionary(), {'id': 99, 'size': 5, 'x': 1, 'y': 2})

    def test_size_property(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1

if __name__ == "__main__":
    unittest.main()
