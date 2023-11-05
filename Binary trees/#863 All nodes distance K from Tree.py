"""https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.
"""

from collections import deque
from collections import defaultdict
from typing import List

class BinaryTree:
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

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

		def findNodeKeepingParents(root, target):
			""" Finds a node in a tree using Breadth-First Search, keeps track of all parents along path.
			Returns target node and stack of parents. """
			queue = deque([(root, None)])  # Queue is a list of sets
			stack = {}  # Stack is a dictionary of nodes and their parents
			while queue:
				node, parent = queue.popleft()
				stack[node.val] = parent
				if node == target: return node, stack
				queue.extend((child, node) for child in [node.left, node.right] if child)
			else: return None, None  # If while statement ends via false condition, return None
		
		target_node, stack = findNodeKeepingParents(root, target)  # Find target node and list of parents up until that depth
		visited = set()

		def step(node, k):
			if k == 0: return [node.val]
			visited.add(node.val)
			ans = []

			for neighbour in [node.left, node.right, stack.get(node.val, None)]:
				if (neighbour) and (neighbour.val not in visited): ans += step(neighbour, k-1)
			return ans
        
		return step(target_node, k)
	

	def distanceK2(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
		"""" Breadth-First Search solution using hashmap to store graph of values """
		def createGraph(node: TreeNode, graph = defaultdict(list)):
			for child in [node.left, node.right]:
				if child:
					graph[child.val].append(node.val)
					graph[node.val].append(child.val)
					createGraph(child)
			return graph
		
		graph = createGraph(root)
		visited = set()

		def step(val, k):
			# Base cases
			if val in visited: return []
			if k == 0: return [val]
			visited.add(val)

			ans = []
			for neighbour in graph[val]: ans += step(neighbour, k-1)
			return ans

		return step(target.val, k)
		
		


root = BinaryTree().generateTree([3,5,1,6,2,0,8,None,None,7,4])
target = BinaryTree().findNode(root, 5)
k = 2
ans = Solution().distanceK2(root, target, k)
print(ans)

a = 2