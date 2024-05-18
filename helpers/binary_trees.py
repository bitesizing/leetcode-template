""" General functions to be used in binary tree problems... """
from collections import deque
from typing import Optional

class TreeNode:
	""" TreeNode class from leetcode. """
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def to_tree(input_values: list) -> TreeNode:
	""" Generates a binary tree from a leetcode tree_list. """
	n = len(input_values)
	tree_map = {}  # Dictionary of node value: [child values]
	empty_count = depth = idx = 0

	# Generate tree_map
	tree_queue = deque(input_values)
	while tree_queue:  # While queue is not empty
		level_count = 0
		for i in range(2**depth - empty_count):  # For each level of the tree
			if not tree_queue: break
			node = tree_queue.popleft()
			if node == None: level_count += 1  # Increment count of each None value on current level
			else:
				r_idx = 2*(idx+1)-empty_count  # Right child index (left child idx = r_idx-1)
				children = [input_values[idx] if idx<n else None for idx in [r_idx-1, r_idx]]  # List of values of left and right children, or None if None
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
	root = unpackChild(input_values[0])
	return(root)