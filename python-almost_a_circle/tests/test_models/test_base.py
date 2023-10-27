#!/usr/bin/python3
import unittest
from models.base import Base
from io import StringIO
import sys

class TestBaseClass(unittest.TestCase):
    """Test methods of BassClass"""

    def test_init_none_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        self.assertEqual(base1.id, 1)

    def test_init_id_passed(self):
        base = Base(7)
        self.assertEqual(base.id, 7)
