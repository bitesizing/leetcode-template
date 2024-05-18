"""https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.
"""

from typing import List
from collections import defaultdict

class Solution:
	def longestSubsequence(self, arr: List[int], difference: int) -> int:
		if arr == []: return 0
	
		dict = defaultdict(int)
		for val in arr: dict[val] = dict[val-difference]+1
		return max(dict.values())

arr = [1,3,5,7]
difference = 1
print(Solution().longestSubsequence(arr, difference))