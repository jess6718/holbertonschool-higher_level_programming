#!/usr/bin/python3
import unittest
from models.base import Base
from io import StringIO
import sys

class TestBaseClass(unittest.TestCase):
    """Test methods of BassClass"""

    def test_init_none_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
