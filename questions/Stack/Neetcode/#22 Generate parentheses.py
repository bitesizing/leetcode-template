"""https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List
import math
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		stack = ""
		n_open, n_closed = n, 0

		def generate(stack, n_open, n_closed):
			if n_open == 0 and n_closed == 0: return [stack]

			result = []
			if n_open > 0:
				result += generate(stack+"(", n_open-1, n_closed+1)
			if n_closed > 0:
				result += generate(stack+")", n_open, n_closed-1)
			return result
		
		return generate(stack, n_open, n_closed)

n = 3
print(Solution().generateParenthesis(n))