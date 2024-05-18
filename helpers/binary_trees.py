""" General functions to be used in binary tree problems... """
from collections import deque
from typing import Optional

class TreeNode:
	""" TreeNode class from leetcode. """
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BinaryTree:
	""" General class of binary tree functions. """

	def isLeaf(self, node: Optional[TreeNode]) -> bool:
		""" Returns True if input node is a leaf, else False """
		return True if (not node.left) and (not node.right) else False
	
	def findNode(self, root, target):
		""" Finds a node in a tree using Breadth-First Search"""
		queue = deque([root])
		while queue:
			node = queue.popleft()
			if node.val == target: return node
			queue.extend(child for child in [node.left, node.right] if child)
		return None
	
	def generateTree(self, tree_list): 
		""" Generates a binary tree from a leetcode tree_list. """
		n = len(tree_list)
		tree_map = {}  # Dictionary of node value: [child values]
		empty_count = depth = idx = 0

		# Generate tree_map
		tree_queue = deque(tree_list)
		while tree_queue:  # While queue is not empty
			level_count = 0
			for i in range(2**depth - empty_count):  # For each level of the tree
				if not tree_queue: break
				node = tree_queue.popleft()
				if node == None: level_count += 1  # Increment count of each None value on current level
				else:
					r_idx = 2*(idx+1)-empty_count  # Right child index (left child idx = r_idx-1)
					children = [tree_list[idx] if idx<n else None for idx in [r_idx-1, r_idx]]  # List of values of left and right children, or None if None
					tree_map[node] = children  # Add child values to dictionary
				idx+=1  # Increment idx

			# Increment empty_count using bitshifting
			empty_count += level_count  # Add null count for each level of the tree to global 'empty_count' var. 
			empty_count << 1  # Leftshift empty_count by 1 to indicate a 'doubling' of each null value
			depth+=1  # Increment depth
		
		# Convert tree_map into actual tree
		def unpackChild(val):
			""" Recursive function to add each child to a tree node. """
			if val == None: return None
			return TreeNode(val, unpackChild(tree_map[val][0]), unpackChild(tree_map[val][1]))
		root = unpackChild(tree_list[0])
		return root