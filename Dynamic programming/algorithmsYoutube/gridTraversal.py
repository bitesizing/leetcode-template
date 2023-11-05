import numpy as np


# %% TRAVERSING AN NxM GRID FROM TOP LEFT TO BOTTOM RIGHT CORNER
# Naive equation with 0(2^n) time complexity
def gridNaive2(n, m):
	if n == 1 or m == 1: return 1
	return gridNaive2(n - 1, m) + gridNaive2(n, m - 1)


# Naive equation THAT CAN HANDLE 0 INPUTS
def gridNaive(n, m):
	def recurse(n, m):
		if n == 1 or m == 1: return 1
		return gridNaive(n-1, m) + gridNaive(n, m-1)
	if n == 0 or m == 0: return 0
	return recurse(n, m)


# Equation using memoisation... cannot handle 0 inputs (easy to adapt if needed)
def calcGrid(n, m, memo={}):
	# NOTE: dicts are reversible - memo[n, m] == memo[m, n], which is great bc a 2,1 grid == a 1,2 grid etc.
	if (n, m) in memo: return memo[n, m]  # Have to input a set bc lists are 'unhashable' (bc order matters)
	if n == 1 or m == 1: return 1
	memo[n, m] = calcGrid(n-1, m, memo) + calcGrid(n, m-1, memo)
	return memo[n, m]


# Fun little experiment to see if i can populate a numpy array - 'bottom-up' instead of recursive 'top-down' approach
def populateGrid(n, m):
	grid = np.ones((n, m), dtype="int32")
	for y in range(n):
		for x in range(m):
			if x == 0 or y == 0: continue
			grid[y, x] = grid[y-1, x] + grid[y, x-1]
	return np.flip(grid)


# Code to see if populateGrid faster than calcGrid - actually it's slower! probably bc of filling / creating the array
def returnFromPopulated(n, m):
	grid = np.ones((n, m), dtype="int32")
	for y in range(n):
		for x in range(m):
			if x == 0 or y == 0: continue
			grid[y, x] = grid[y-1, x] + grid[y, x-1]
	return grid[n-1, m-1]


