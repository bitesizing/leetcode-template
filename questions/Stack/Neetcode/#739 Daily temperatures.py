"""https://leetcode.com/problems/daily-temperatures/
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

from typing import List
import math
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		n = len(temperatures)
		stack = []
		days_to_wait = [0]*n

		for h_idx in range(n):
			while stack and temperatures[h_idx] > stack[-1][0]:
				l_idx = stack.pop()[1]
				days_to_wait[l_idx] = h_idx - l_idx
			stack.append((temperatures[h_idx], h_idx))
		return days_to_wait


temperatures = [73]
print(Solution().dailyTemperatures(temperatures))