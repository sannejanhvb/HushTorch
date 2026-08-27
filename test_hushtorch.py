# test_hushtorch.py
"""
Tests for HushTorch module.
"""

import unittest
from hushtorch import HushTorch

class TestHushTorch(unittest.TestCase):
    """Test cases for HushTorch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HushTorch()
        self.assertIsInstance(instance, HushTorch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HushTorch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
