"""https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

from typing import List
import math
from collections import deque, defaultdict

class Solution:	
	def longestConsecutive2(self, nums: List[int]) -> int:
		if nums == []: return 0
		d = {}
		for num in nums:
			if num in d: continue
			d[num] = num

			min_val = max_val = num
			if (num-1) in d:
				min_val = num-1
				while d.get(min_val) < min_val: min_val = d.get(min_val)
			if (num+1) in d:
				max_val = num+1
				while d.get(max_val) > max_val: max_val = d.get(max_val)
			d[min_val] = max_val
			d[max_val] = min_val
		print(d)
		return max([key-val for key, val in d.items()])+1
	
	def longestConsecutive(self, nums: List[int]) -> int:
		numset = set(nums)
		longest = 0
		for num in numset:
			if num-1 not in numset:
				length=1
				while num+length in numset: length+=1
				longest = max(longest, length)
		return longest

				
		
	
nums = [100,4,200,1,3,2]
print(Solution().longestConsecutive(nums))