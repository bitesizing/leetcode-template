# %%
from typing import List, Optional
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop
from .helpers import *

""" Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
�
Constraints:

- -231 <= x <= 231 - 1


"""

# Code
class Solution:
    def reverse(self, x: int) -> int:
        pass




# Tests (ignore)
examples_list = [{'inputs': {'x': 123}, 'output': 321}, {'inputs': {'x': -123}, 'output': -321}, {'inputs': {'x': 120}, 'output': 21}]
run_tests(
    examples_list = examples_list,
    function = Solution().reverse)