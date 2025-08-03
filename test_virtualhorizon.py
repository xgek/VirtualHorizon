# test_virtualhorizon.py
"""
Tests for VirtualHorizon module.
"""

import unittest
from virtualhorizon import VirtualHorizon

class TestVirtualHorizon(unittest.TestCase):
    """Test cases for VirtualHorizon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VirtualHorizon()
        self.assertIsInstance(instance, VirtualHorizon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VirtualHorizon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
