#!/usr/bin/python3
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test methods of BassClass"""

    def test_init_none_id(self):
        """Test whether incremental works none_id passed in"""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        self.assertEqual(base1.id, 1)
        self.assertNotEqual(base1.id, base2.id)
        self.assertEqual(base1.id+1, base2.id)

    def test_init_id_passed(self):
        """Test whether Base returns id if a number passed in"""
        base = Base(7)
        self.assertEqual(base.id, 7)
