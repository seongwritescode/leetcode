"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
    	if len(strs) == 1:
    		return strs[0]
    	common_str = ""
    	check_str = ""
    	str_1th = strs[0]
    	idx = 0
    	param_check = 0
    	check_str = ""
    	while idx < len(str_1th):
    
    		if param_check == 0:	
    			if len(check_str) > len(common_str):
	    			common_str = check_str
    			check_str += str_1th[idx]

    		else:
    			check_str = str_1th[idx]
    			param_check = 0
    		for ele in strs:
    			if check_str not in ele: 
    				param_check = 1
    				break

    		idx += 1
    	print(common_str)
    	return common_str	


solution = Solution()
print(solution.longestCommonPrefix(strs = ["reflower","flow","flight"]))
        