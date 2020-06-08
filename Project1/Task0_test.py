#Test file for Task0.py

import unittest
import unittest.mock as mock
from unittest.mock import mock_open
from Task0 import SumMyNumbers
from Task0 import myfunction


class TestSum(unittest.TestCase):
	def test_mysum(self):
		self.assertEqual(SumMyNumbers(2, 2, 3), 6, "Should be 6")
	
	#def test_myfunction(mock_open):
	#	mock.open.return_value.__enter__ = mock_open
	#	mock_open.return_value.__iter__ = mock.Mock(
        #		return_value = iter(['12characters', '13_characters']))
    	#	answer = myfunction('foo')
    	#	self.assertEqual(answer, 13, "Should be 13")

if __name__ == '__main__':
	unittest.main()


