#!/usr/bin/python3
"""Module for testing Square class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test methods of SquareClass"""

    def setUp(self):
        """reset the base class private attribute"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """clean up the class private attribute"""
        Base._Base__nb_objects = None

    def test_init_with_valid_inputs(self):
        """Test init method"""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.id, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.id, 2)

        s2 = Square(1, 2, 3)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 3)

        s3 = Square(1, 2, 3, 4)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 4)

    def test_init_with_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Square("Pikachu", 7, 7)
        with self.assertRaises(TypeError):
            Square(7, "Pikachu", 7)
        with self.assertRaises(TypeError):
            Square(7, 7, "Pikachu")
        with self.assertRaises(ValueError):
            Square(-7, 7, 7)
        with self.assertRaises(ValueError):
            Square(7, -7, 7)
        with self.assertRaises(ValueError):
            Square(7, 7, -7)
        with self.assertRaises(ValueError):
            Square(0, 7, 7)

    # def test_str_return(self):
    # def test_size(self):
    # def test_update(self):
    # def test_to_dictionary(self):
    # def test_save_to_file(self):
    # def test_from_json(self):
    # def test_create(self):
