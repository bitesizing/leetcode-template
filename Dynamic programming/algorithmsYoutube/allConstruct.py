# Return all the ways to construct a string...
from typing import List

# Returns one way to construct a target string from a set of substrings, including memoisation
def howConstruct(target: str, strings: List[str], memo={}) -> int:
	# Base case
	if target in memo: return memo[target]
	if target == "": return []

	# Loop through each index in the target string and check if there is a string starting at that index
	target_len = len(target)
	sum = 0
	for string in strings:
		sub_len = len(string)
		# Check if index in range, then compare START of target to string (CAN GET AWAY WITH ONLY COMPARING START!!)
		if target.startswith(string):
			# Remove string from target and recurse using new target string
			new_target = target[sub_len:]
			child = howConstruct(new_target, strings)
			if child is not None: return [*child + [string]]
	return None


# Returns all constructs in order>:)
def allConstruct(target: str, word_bank: List[str], memo={}) -> List[List[str]]:
	if target in memo: return memo[target]  # First we check if value in memo dict object
	if target == "": return [[]]  # Base case when starting a valid chain: return empty list of lists

	# Define variables
	target_len = len(target)
	all_combinations = []  # Empty list that we will append valid combinations to

	# Loop through and remove valid strings from end of target (so final answer is in correct order), then recall
	for word in word_bank:
		sub_len = len(word)

		# Compare end of target to current string to check validity...
		if target.startswith(word):
			# Remove string from start of target and recurse using new target string
			new_target = target[sub_len:]
			combinations = allConstruct(new_target, word_bank, memo)

			# Append current string to each combination in combinations, then concat. into all_combinations
			target_ways = map((lambda combination: [word] + combination), combinations)
			all_combinations += target_ways

	# Assign to memo dict and return
	memo[target] = all_combinations
	return memo[target]

target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz"
word_bank = ["a", "aa", "aaa", "aaaa", "aaaaa"]
result = allConstruct(target, word_bank)
print(result)

# TIME AND SPACE COMPLEXITY...
# m = len(target), n = len(word_bank)
# height = m; worst case we are subtracting 1 char each layer so max m layers
# O(m^n) nodes, because each node in m layers splits into n nodes
# This means m^n maximum subarrays in our output... one for each node on the bottom layer
# So have to return a result that is exponential in size... can't get better than exponential time complexity
# Space complexity is O(m) (don't include size of output into space complexity... (?)) 

