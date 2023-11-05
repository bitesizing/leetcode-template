# Count the number of ways a set of substrings can combine to form a target string
from typing import List


# Memoisation attempt (gonna stop putting the naive version separately now
def countConstruct(target: str, strings: List[str], memo={}) -> int:
	# Base case
	if target in memo: return memo[target]
	if target == "": return 1

	# Loop through each index in the target string and check if there is a string starting at that index
	target_len = len(target)
	sum = 0
	for string in strings:
		sub_len = len(string)
		# Check if index in range, then compare START of target to string (CAN GET AWAY WITH ONLY COMPARING START!!)
		if target.startswith(string):
			# Remove string from target and recurse using new target string
			new_target = target[sub_len:]
			sum += countConstruct(new_target, strings, memo)  # Add value returned by recursive call to sum
	memo[target] = sum
	return sum


target = "abcdef"
strings = ["ab", "abc", "cd", "def", "abcd"]
result = countConstruct(target, strings)
print(result)
