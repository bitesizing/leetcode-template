""" https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.
"""

from typing import List
from collections import deque

class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		lo, hi, max_length = 0, 0, 0
		group_lengths = deque([0, 0])

		while (lo < len(nums)) and (hi < len(nums)):
			if nums[lo] == 1:
				while (hi < len(nums)) and (nums[hi] == 1): hi+=1  # Find next 'non-1' integer
				group_lengths.popleft()
				group_lengths.append(len(nums[lo:hi]))
				max_length = max(max_length, sum(group_lengths))
				lo = hi+1  # Set lo to the integer after hi
			else:
				while (lo < len(nums)) and (nums[lo] != 1): lo+=1  # Find next '1' integer
				group_lengths.popleft()
				group_lengths.append(len(nums[lo:hi]))
			hi+=1

		if max_length == len(nums): max_length -= 1  # -1 if max_length == len(nums) bc an element MUST be removed
		return max_length


nums = [1,1,0,0,1]
print(f"{Solution().longestSubarray(nums)}")


class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		n = len(nums)  # The size of the input array
		lo, zeros, max_length = 0, 0, 0

		for hi in range(n):
			if nums[hi] == 0:
				zeros += 1  # Increment the count of zeroes

			# Adjust the window to maintain at most one zero in the subarray
			while zeros > 1:
				if nums[lo] == 0:
					zeros -= 1  # Decrement the count of zeroes
				lo += 1  # Move the left pointer to the right

			# Calculate the length of the current subarray and update the maximum length
			max_length = max(max_length, hi - lo)

		# If the entire array is the subarray, return the size minus one; otherwise, return the maximum length
		return max_length - 1 if max_length == n else max_length

