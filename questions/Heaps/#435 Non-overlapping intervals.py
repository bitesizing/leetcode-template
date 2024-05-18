"""https://leetcode.com/problems/non-overlapping-intervals/
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		n = len(intervals)
		intervals.sort()  # Sort ascending for 0th index, descending for 1st index.

		lo = n_removed = 0
		for hi in range(1, n):
			if intervals[lo][1] > intervals[hi][0]:
				lo = min(lo, hi, key=lambda x: intervals[x][1])
				n_removed += 1
			else:
				lo = hi
		return n_removed
				
intervals = [[-73, -26], [-65, -11], [-63, 2], [-62, -49], [-52, 31], [-40, -26], [-31, 49], [30, 47], [58, 95], [66, 98], [82, 97], [95, 99]]
print(Solution().eraseOverlapIntervals(intervals))