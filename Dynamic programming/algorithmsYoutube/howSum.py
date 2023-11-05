# howSum is very similar to canSum but it needs to return a set of numbers that sum to the target...
# Should be able to use the same architecture as before but storing values as we go...
# We always store one of the values so maybe we can just append them in the return call...
from typing import List


# First attempt at a modified howSum function
def howSum(target: int, nums: List[int], memo={}):
	if target in memo: return memo[target]
	if target == 0: return []
	elif target < 0: return None

	# Loops through and returns true as soon as a true value is given
	for num in nums:
		# Don't need to assign to memo if true because we are exiting the parent function immediately
		list_out = howSum((target - num), nums, memo)
		if list_out is not None:
			list_out.append(num)
			return list_out

	# If no true values given, set as false and return
	memo[target] = None
	return None


# Brute force attempt to return all sums to the target value
def allSum(target: int, nums: List[int]):
	if target == 0: return [[]]  # Return a list with an empty list inside
	elif target < 0: return None

	all_sum_current = []
	# Loops through and returns true as soon as a true value is given
	for num in nums:
		# Recursive call
		tmp_result = allSum((target - num), nums)  # Result should be a list of lists
		if tmp_result is not None:  # If there is a list that sums to the target...
			# tmp_result will be a list of lists...
			for sublist in tmp_result:
				all_sum_current.append([*sublist, num])
	return all_sum_current


# allSum func. using memoisation, and tuples to remove duplicate (reordered) solutions ongoing...
def memoAllSum(target: int, nums: List[int], memo={}):
	if target in memo: return memo[target]
	if target == 0: return [[]]  # Return a list with an empty list inside
	elif target < 0: return None

	all_sum_current = set()
	# Loops through and returns true as soon as a true value is given
	for num in nums:
		# Recursive call
		tmp_result = memoAllSum((target - num), nums, memo)  # Result should be a list of lists
		if tmp_result is not None:  # If there is a list that sums to the target...
			# tmp_result will be a list of lists...
			for sublist in tmp_result:
				unpacked = (*sublist, num,)  # Unpack as tuple: need comma at the end or single values will be registered as int
				all_sum_current.add(tuple(sorted(unpacked)))   # Sort tuple then convert back to tuple to remove repeats
	memo[target] = all_sum_current
	return memo[target]

nums = [1, 2]
target = 2
#print(allSum(target, nums))
print(memoAllSum(target, nums))
