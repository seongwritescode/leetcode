import unittest
from problem_28 import Solution

class SearchInsertTest(unittest.TestCase):
	solution = Solution()
	def test_insert_test(self):
		self.assertEqual(2, solution.searchInsert(nums=[1,3,5,6],target=5))
		self.assertEqual(1, solution.searchInsert(nums = [1,3,5,6], target = 2))
		self.assertEqual(4, solution.searchInsert(nums = [1,3,5,6], target = 7))

		

