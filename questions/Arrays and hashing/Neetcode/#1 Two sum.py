"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution:
	def twoSum(self, nums, target):
		""" FAST hash table approach:)) """
		hash_table = {}  # Initialise empty dict / hash table

		for idx, num in enumerate(nums):
			complement = target - num  # For each num, calc what is needed to sum to the target
			if complement in hash_table: return [hash_table[complement], idx]  # If complement exists in table, return the pair
			else: hash_table[num] = idx  # Else add the complement to the table. Hashtable lookup is O(1) so overall this is O(N)
		return 0


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
