#Test file for Task0.py

import unittest
import unittest.mock as mock
from Task0 import fileHeadAndTail

class TestSum(unittest.TestCase):
  def test_fileHeadAndTail(self):
    with mock.patch('builtins.open', mock.mock_open(read_data='FirstLine\nSecondLine\nThirdLine')):
      results = fileHeadAndTail('dev/null')
      self.assertEqual(results['first_record'][0], 'FirstLine', "Should be FirstLine")
      self.assertNotEqual(results['first_record'][0], 'SecondLine', "Should not be SecondLine")
      self.assertEqual(results['last_record'][0], 'ThirdLine', "Should be ThirdLine")

if __name__ == '__main__':
  unittest.main()


