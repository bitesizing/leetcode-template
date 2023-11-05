"""https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""

from typing import List

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		prefix = suffix = 1
		answer = [1]*n

		for i in range(n):
			answer[i] *= prefix
			prefix *= nums[i]

			answer[n-i-1] *= suffix
			suffix *= nums[n-i-1]

		return answer


nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))
