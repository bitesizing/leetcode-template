# Given a target and an input list, return the shortest list of numbers that sum to the list.
# If no numbers sum, return None
from typing import List


# Brute force function adapted from allSum - seems to work pretty elegantly:)
def bestSum(target:int, nums:List[int]):
	if target == 0: return []
	if target < 0: return None

	# Store all child returns (each a single list) in a list using comprehension
	shortest = []
	for num in nums:
		child = bestSum((target-num), nums)
		if child is not None:
			child.append(num)   # Append the value needed to subtract to get to a true sum from the target
			if (shortest == []) or (len(child) < len(shortest)):
				shortest = child
	return (shortest if shortest != [] else None)  # Return none if no children return '[]'


# Adapted function using memoisation - works well!
def bestSumMemo(target:int, nums:List[int], memo={}):
	# Base cases and memo access
	if target in memo: return memo[target]
	if target == 0: return []
	if target < 0: return None

	# Store all child returns (each a single list) in a list using comprehension
	shortest = None
	for num in nums:
		child_combination = bestSumMemo((target-num), nums, memo)
		if child_combination is not None:
			combination = child_combination + [num]  # Append current num to make our full combination
			if (shortest is None) or ((len(combination)) < len(shortest)):
				shortest = combination
	memo[target] = shortest  # Store 'none' value if no children return lists
	return memo[target]


target = 205
nums = [7, 6, 24, 102]
result = sorted(bestSumMemo(target, nums), reverse=True)
print(f"Shortest way to sum to {target} with values: {nums}...")
print(result)