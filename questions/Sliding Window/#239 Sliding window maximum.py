"""https://leetcode.com/problems/sliding-window-maximum/
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

# Each number could store what the max BECOMES after it leaves

class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		sliding_nums = [[] for i in range(len(nums))]  # Could also initialise as empty? Saves having to loop... 
		stack = []

		for idx, num in enumerate(nums):
			while (stack) and (idx-stack[-1][1] > k) and (stack[-1][0] <= num):
				tmp_val, tmp_idx = stack.pop()
				sliding_nums[tmp_idx] = (tmp_val, num)

			stack.append((num, idx))
		
		# Clear rest of stack
		while stack:
			tmp_val, tmp_idx = stack.pop()
			sliding_nums[tmp_idx] = (tmp_val)


			

		


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))