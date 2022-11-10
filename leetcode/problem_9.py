"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        if y == str(x):
            return True
        return False




solution = Solution()
solution.isPalindrome(-1221)        
