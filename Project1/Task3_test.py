#Test file for Task3.py

import unittest
from Task3 import AggregateBangaloreCallTargets

class TestTask3(unittest.TestCase):
  def test_AggregateBangaloreCallTargets(self):
      testData = [
        ['(080)1234', '(040)123', '', 0],
        ['(080)5678', '(040)123', '', 0],
        ['(080)1234', '123 4567', '', 0],
        ['(080)1234', '14056789', '', 0],
        ['(123)4567', '987 654', '', 0],
      ]
      results = AggregateBangaloreCallTargets(testData)
      self.assertEqual(results['140'], 1, "Target 140 should be called once")
      self.assertEqual(results['(040)'], 2, "Target 040 should be called twice")
      self.assertEqual(results['123 '], 1, "Target 123 should be called once")
      self.assertNotEqual(results['987 '], 1, "Target 987 should be zero")

if __name__ == '__main__':
  unittest.main()
