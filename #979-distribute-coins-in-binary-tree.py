# %%
from typing import List, Optional
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop
from .helpers import *

""" Distribute Coins in Binary Tree

Description:
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin.

Constraints:
- The number of nodes in the tree is n.
- 1 <= n <= 100
- 0 <= Node.val <= n
- The sum of all Node.val is n.

"""

# Code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        pass




# Tests (ignore)
examples_list = [{'inputs': {'root': [3, 0, 0]}, 'output': 2}, {'inputs': {'root': [0, 3, 0]}, 'output': 3}]
run_tests(
    examples_list = examples_list,
    function = Solution().distributeCoins)