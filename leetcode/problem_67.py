"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
    	remem = 0
    	idx = 0 
    	result  = ''
    	while (idx < len(a)) and (idx < len(b)):
    		
    		if a[len(a) - 1 - idx] == '1' and b[len(b) - 1 - idx] == '1':
    			if remem == 0:
	    			result = '0' + result
    				remem = 1
    			else:
    				
    				result = '1' + result
    		else:
    			if remem == 1 and  a[len(a) - 1 - idx] == '0' and b[len(b) - 1 - idx] == '0':
    				result = '1' + result
    				remem = 0
    			elif (remem == 1) and (a[len(a) - 1 - idx] != '0' or b[len(b) - 1 - idx] != '0'):

    				result = '0' + result
    			elif remem == 0 and  a[len(a) - 1 - idx] == '0' and b[len(b) - 1 - idx] == '0':
    				result = '0' + result
    			else:
    				result = '1' + result
    		idx += 1 
    	print(remem, result)
    	if idx == len(b):
    		if remem == 1:
    			for i in range(len(a) - 1 - idx, -1, -1):
    				if a[i] == '1':
    					if remem == 1:
    						result = '0' + result
    					else:
    						result = '1' + result
    						remem = 0
    				else:
    					if remem == 1:
	    					result = '1' + result
    						remem = 0
    					else: 
    						result = '0' + result
    		else:
    			result = a[:len(a) - idx] + result
    	elif idx == len(a) :
    		if remem == 1:
    			for i in range(len(b)  - 1 - idx, -1, -1):

    				if b[i] == '1':
    					if remem == 1:
    						result = '0' + result
    					else:
    						result = '1' + result
    						remem = 0
    				else:
    					if remem == 1:
	    					result = '1' + result
    						remem = 0
    					else: 
    						result = '0' + result
    		else:
    			result = b[:len(b) - idx] + result
    	if remem == 1:
    		result = '1' + result		

    	return result
if __name__ == '__main__':

    solution = Solution()
    print(solution.addBinary(b = "110010", a = "10"))

