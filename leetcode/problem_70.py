"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
class Solution:
	def cal_factorial(self, num):
		factorial = 1
		for i in range(1,num + 1):
			factorial = factorial*i
		return factorial

	def cal_permutation(self, n, k):
   		count = self.cal_factorial(n) / (self.cal_factorial(n - k) * self.cal_factorial(k))
   		return count 

	def climbStairs(self, n: int) -> int:
		if n == 1:
			return n

		max_2_steps = int(n/2)

		ways = 0
		for i in range(0, max_2_steps+1):
			ways += self.cal_permutation(n-i-1, i+1)

		ways = int(ways)
		return ways +1

if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(n = 4))
