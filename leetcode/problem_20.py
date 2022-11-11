"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack_char = [s[0]]
        char_ = ['(','[','{']
        char_order = [')','[','}']
        for idx in range(1, len(s)):
        	if not stack_char:
        		stack_char.append(s[idx])
        	elif (stack_char[-1] in char_ and s[idx] in char_) or (stack_char[-1] in char_order and s[idx] in char_order):
        		stack_char.append(s[idx])
        	else:

        		char_compare = stack_char.pop() 
        		if (char_compare not in char_):
        			return False

        		elif  ((char_compare == '(' and s[idx] != ')') or (char_compare == '[' and s[idx] != ']') or (char_compare == '{' and s[idx] != '}')):
        			return False
       	if stack_char:
       		return False
        return True

if __name__ == '__main__':

	solution = Solution()
	print(solution.isValid(s = "(("))



