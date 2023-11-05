"""https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

from typing import List
import math
from collections import deque, defaultdict

class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		match = {")":"(", "}":"{", "]":"["}
		for char in s:
			if char in ["(", "[", "{"]:
				stack.append(char)
			else:
				if not stack or match[char] != stack.pop(): return False
		return False if stack else True

s = "()"	
print(Solution().isValid(s))