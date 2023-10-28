#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test methods of RectangleClass"""

    def setUp(self):
        """reset the base class private attribute"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """clean up the class private attribute"""
        Base._Base__nb_objects = None

    def test_init_with_valid_inputs(self):
        """Test init method"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)

    def test_init_with_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Rectangle("Pikachu", 7, 7, 7)
        with self.assertRaises(TypeError):
            Rectangle(7, "Pikachu", 7, 7)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, "Pikachu", 7)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, 7, "Pikachu")
        with self.assertRaises(ValueError):
            Rectangle(-7, 7, 7, 7)
        with self.assertRaises(ValueError):
            Rectangle(7, -7, 7, 7)
        with self.assertRaises(ValueError):
            Rectangle(7, 7, -7, 7)
        with self.assertRaises(ValueError):
            Rectangle(-7, 7, 7, -7)
        with self.assertRaises(ValueError):
            Rectangle(0, 7, 7, 7)
        with self.assertRaises(ValueError):
            Rectangle(7, 0, 7, 7)

    def test_area(self):
        """test the area method"""
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)
