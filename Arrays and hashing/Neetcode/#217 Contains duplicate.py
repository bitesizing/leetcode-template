"""https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

from typing import List

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		""" Very simple one-line solution using hash-sets """
		return len(nums) != len(set(nums))

	def containsDuplicate2(self, nums: List[int]) -> bool:
		""" Slightly faster set returning true ASAP... actually slower under the hood! Wonder why? Faster to set a whole array at once... """
		seen = set()
		for num in nums:
			if num in seen: return True
			seen.add(num)
		return False

nums = [1,2,3,4]
print(Solution().containsDuplicate(nums))
