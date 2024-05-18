"""https://leetcode.com/problems/guess-number-higher-or-lower-ii/
We are playing the Guessing Game. The game will work as follows:
    I pick a number between 1 and n.
    You guess a number.
    If you guess the right number, you win the game.
    If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
    Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick."""

import math

class Solution:
	""" Working dynamic programming leetcode solution. """
	def getMoneyAmount(self, n: int) -> int:
		""" Solution to find the 'min-max', or the maximum amount of money needed in the most efficient (minimum) tree. """
		full_range = list(range(1+(n%2), n, 2))  # Range counting up in 2 with opposite 'evenness' to n; each inner (non-leaf) node
		memo = {}  # Initialise dict

		def recurse(local_range) -> int:
			# Check memo
			if tuple(local_range) in memo: return memo[tuple(local_range)]

			# Base cases
			if len(local_range) == 0: return 0
			if len(local_range) == 1: return local_range[0]

			# Recursion using max / min function:
			midpoint = math.ceil((len(local_range) - 1) / 2)  # Find the midpoint of local range
			local_max = math.inf
			for i, val in enumerate(local_range[midpoint:]):  # Find the 'optimum' child node using recursion. Optimum child will never be lower than the midpoint so start here... 
				local_max = min(local_max, max(recurse(local_range[:midpoint + i]), recurse(local_range[i + midpoint + 1:])) + val)  # Return MINIMUM of current local_max and MAXIMUM value for each branch of the tree (left and right)

			memo[tuple(local_range)] = local_max
			return local_max

		return recurse(full_range)


class MoneyTree:
	""" Attempts to expand and visualise the problem... """
	def __init__(self):
		self.binary_tree = {}
		self.root = None

	def initialiseFullTree(self, n):
		max, paths = self.makeTreeFromRange(n)
		good_paths = self.convertTree(paths)
		self.visualise_tree(self.root)

	# Tryna make it visualise....
	def makeTreeFromRange(self, n: int) -> int:
		full_range = list(range(n%2+1, n, 2))  # Range to n-1 of numbers with opposite oddness to n... bc of how graphs are constructed
		memo = {}

		def recursionSubfunc(local_range):
			# Check memo
			if tuple(local_range) in memo: return memo[tuple(local_range)]

			# Base case
			if len(local_range) == 0: return (0, {})
			if len(local_range) == 1: return (local_range[0], {local_range[0]: [local_range[0]]})

			# Recursion using max / min function:
			start_idx = math.ceil((len(local_range) - 1) / 2)  # Find the midpoint of local range
			local_max, local_paths = math.inf, {}
			for i, val in enumerate(local_range[start_idx:]):
				left_max, left_paths = recursionSubfunc(local_range[:start_idx + i])
				right_max, right_paths = recursionSubfunc(local_range[i + start_idx + 1:])

				lr_max = max(left_max, right_max) + val
				if lr_max < local_max:  # Min function; if there is a new min max
					local_max = lr_max  # Update local max
					local_paths = {**left_paths, **right_paths, val: local_range}  # Combine left, right, and 'combo' paths

			memo[tuple(local_range)] = local_max, local_paths  # Add to memo
			return (local_max, local_paths)

		return recursionSubfunc(full_range)

	def convertTree(self, paths):
		tree_dict = {}
		self.root = max(paths, key=lambda x: len(set(paths[x])))
		vals = paths.keys()

		def recurse(vals):
			root = max({k: paths[k] for k in vals}, key=lambda x: len(set(paths[x])))  # Finds the key with the most values
			left_vals = [x for x in vals if x < root]
			right_vals = [x for x in vals if x > root]

			tree_dict[root] = []
			for i in [left_vals, right_vals]:
				if i != []: tree_dict[root].append(recurse(i))
			return root

		recurse(vals)
		self.binary_tree = tree_dict
		return tree_dict

	def visualise_tree(self, root, level=0):
		if root not in self.binary_tree:
			return
		children = self.binary_tree[root]
		prefix = "  " * level
		print(f"{prefix}- {root}")
		for child in children:
			self.visualise_tree(child, level + 1)




n = 60
#print(Solution().getMoneyAmount(n))
tree_class = MoneyTree()
my_tree = tree_class.initialiseFullTree(n)




