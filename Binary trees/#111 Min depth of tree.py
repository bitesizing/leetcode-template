"""https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isLeaf(self, node: Optional[TreeNode]) -> bool:
		""" Returns True if input node is a leaf, else False """
		return True if (not node.left) and (not node.right) else False

	def minDepth(self, root: Optional[TreeNode]) -> int:
		""" Calculates the minimum depth from the root node (inclusive) needed to find a leaf """
		if not root: return 0  # additional check if tree is empty
		queue = deque([root])  # allows faster pop left
		depth = 1

		while True:  # Each iteration of the while loop corresponds to one level of the tree
			for i in range(len(queue)):  # Each step in the for loop corresponds to one node in each level
				node = queue.popleft()
				if self.isLeaf: return depth  # Check if node is a leaf
				[queue.append(child) for child in [node.left, node.right] if child]
			depth += 1
