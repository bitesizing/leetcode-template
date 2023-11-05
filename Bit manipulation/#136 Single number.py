"""https://leetcode.com/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List

class Solution:
	""" Solution using bitwise XOR operator, which works to simulate mod 2 for each individual bit.
	This means that numbers which appear twice will cancel out, leaving only the unique number. """

	def singleNumber(self, nums: List[int]) -> int:
		ans = 0
		for i in range(len(nums)):
			ans ^= nums[i]  # ans = itself + the bitwise XOR... mod 2 for each binary unit... means that if there are 2 of the same bit, it resets to 0
		return ans

nums = [4, 2, 1, 2, 1]
print(Solution().singleNumber(nums))



