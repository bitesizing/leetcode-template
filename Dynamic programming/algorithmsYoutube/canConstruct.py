# Return true if you can construct a target string with any combination of target substrings... 
from typing import List


# First attempt at a brute force algorithm
def canConstructNaive(target: str, strings: List[str]) -> bool:
	# Base case
	if target == "": return True
	
	# Loop through each index in the target string and check if there is a string starting at that index
	target_len = len(target)
	for string in strings:
		sub_len = len(string)
		# Check if index in range, then compare START of target to string (CAN GET AWAY WITH ONLY COMPARING START!!)
		if target.startswith(string):
			# Remove string from target and recurse using new target string
			new_target = target[sub_len:]
			child = canConstructNaive(new_target, strings)
			if child == True: return True  # can fast return if true
	return False


# Attempt to introduce memos...
def canConstructMemo(target: str, strings: List[str], memo={}) -> bool:
	if target in memo: return memo[target]  # Check if in memo
	if target == "": return True  # Base case

	# Loop through each index in the target string and check if there is a string starting at that index
	target_len = len(target)
	for string in strings:
		sub_len = len(string)
		# Check if target starts with the string (CAN GET AWAY WITH ONLY COMPARING START!!)
		if target.startswith(string):
			# Remove string from target and recurse using new target string
			new_target = target[sub_len:]
			child = canConstructNaive(new_target, strings)
			if child == True: return True  # can fast return if true
	memo[target] = False
	return False


target = "skateboard"
strings = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
result = canConstructMemo(target, strings)
print(result)