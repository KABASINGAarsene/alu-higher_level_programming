#!/usr/bin/python3


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_initialization(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(100)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 100)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_save_to_file(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file_no_file(self):
        self.assertEqual(Base.load_from_file(), [])

if __name__ == "__main__":
    unittest.main()
