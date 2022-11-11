"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        flag = 0
        middle = int(len(nums)/2)
        end = len(nums)-1
        start = 0

        if target <= nums[start]:
            return start 
        if target > nums[end]:
            return end+1

        while end >= start:

            if (target <= nums[middle] and target > nums[middle-1]):
                
                flag = 1
                return middle
            elif (target >= nums[middle] and target <= nums[middle+1]):
                
                flag = 1
                return middle+1 
            elif target > nums[middle]:
                
                start = middle 

                middle = int((end + start) / 2)
            elif target <= nums[middle]:
                
                end = middle

                middle = int((end + start) / 2)

            
        return middle

if __name__ == '__main__':

    solution = Solution()
    print(solution.searchInsert(nums = [1,4,6,7,8,9], target = 6))
    # print(solution.searchInsert(nums=[1,3,5,6],target=5))

