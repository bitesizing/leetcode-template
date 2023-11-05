"""https://leetcode.com/problems/evaluate-reverse-polish-notation/
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

from typing import List
from math import floor, ceil
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		for token in tokens:
			if token not in ["+", "-", "/", "*"]:
				stack.append(int(token))
			else:
				x = stack.pop()
				y = stack.pop()

				if   token == "+": stack.append(x+y)
				elif token == "*": stack.append(x*y)
				elif token == "-": stack.append(y-x)
				elif token == "/": stack.append(int(y/x))
		return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))