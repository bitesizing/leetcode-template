"""https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.
"""

from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	""" ldkfssdfhjkdfs """
	def combine(self, n: int, k: int) -> List[List[int]]:
		memo = {}
		current = set()

		def backtrack(min_i):
			current_tup = tuple(sorted(current))
			if current_tup in memo:
				print(memo[current_tup])
				return memo[current_tup]
			if len(current) == k: return [list(current)]  # Return list of lists bc output format
			combinations = []

			for i in range(min_i, n+1):
				if i not in current:
					current.add(i)
					for combination in backtrack(i): combinations.append(combination)
					current.remove(i)
			if 1 < len(current) < k-1: memo[current_tup] = combinations
			return combinations
		return backtrack(1)




n = 4
k = 2
print(Solution().combine(n, k))