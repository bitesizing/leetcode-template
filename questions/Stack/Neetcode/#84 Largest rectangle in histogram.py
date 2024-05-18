"""https://leetcode.com/problems/largest-rectangle-in-histogram/
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

from typing import List, Optional
import math
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	"""Intuition:
		- Use a monotonic increasing stack. 
		- Store (height, bar_number) in stack for each height if it's bigger than the one before it. 
		- This is because we need to keep track of multiple areas (the shorter but wider area && taller but thinner area). 
		- If current_height is smaller than previous, we can calculate any rectangles with height > current_height.
		- Pop while current_height < heights[-1], area = height * current_idx - bar_number (width).
		- After we have iterated through all bars, need to process remaining values in the stack. We can just calculate the area in the same way for every value left in the stack.
	"""
	def largestRectangleArea(self, heights: List[int]) -> int:
		""" Returns the largest possible area of a rectangle within a histogram where bar_heights = heights and bar_widths === 1"""
		stack = []  # Monotonic increasing stack; increasing values bottom to top
		largest_area = 0
		for i, curr_height in enumerate(heights):
			starting_idx = i
			while stack and curr_height < stack[-1][0]:
				pop_height, starting_idx = stack.pop()  # Pop starting_idx of HIGHER value, assign to new lower value since area 'shared'
				largest_area = max(largest_area, pop_height*(i-starting_idx))
			if not stack or curr_height > stack[-1][0]: stack.append((curr_height, starting_idx))

		while stack:
			pop_height, starting_idx = stack.pop()
			largest_area = max(largest_area, pop_height*(i-starting_idx+1))
		return largest_area

heights = [2,1,2]
print(Solution().largestRectangleArea(heights))