"""https://leetcode.com/problems/minimum-size-subarray-sum/
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead."""

from typing import List
import math

class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		if sum(nums) < target: return 0
		n = len(nums)
		min_length = n
		current_total, lo = 0, 0

		for hi in range(n):
			current_total += nums[hi]
			while current_total >= target:
				min_length = min(min_length, hi-lo+1)
				current_total -= nums[lo]
				lo +=1
		return min_length

target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))

