import unittest
from problem_28 import Solution

class SearchInsertTest(unittest.TestCase):
	solution = Solution()
	def test_insert_test(self):
		self.assertEqual(0, self.solution.searchInsert(nums=[1],target=1))
		self.assertEqual(2, self.solution.searchInsert(nums=[1,3,5,6],target=5))
		self.assertEqual(1, self.solution.searchInsert(nums = [1,3,5,6], target = 2))
		self.assertEqual(4, self.solution.searchInsert(nums = [1,3,5,6], target = 7))
		self.assertEqual(2, self.solution.searchInsert(nums = [1,4,6,7,8,9], target = 6))
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
		

