# Given an input array and a target, return whether the values in the input array can sum to the target
# No non-negative values and all values are integers

from typing import List


# Naive summing function using some hard-to-parse comprehension...
# ONLY WORKS WITH UNIQUE NUMBERS BECAUSE OF THE USE OF SETS
def canSumNaive(target: int, nums: List[int], exclude=set()) -> bool:
    # Return true if the sum of numbers in the list are equal to the target
    curr_sum = sum([val for val in nums if val not in exclude])
    if curr_sum == target: return True
    
    # Return true if any of the sub-sums are true
    for val in nums:
        if (val not in exclude) and (canSumNaive(nums, target, exclude.union({val})) is True):
            return True
    return False

# Expansion to the previous function adding memoisation
def canSumMine(target: int, nums: List[int], exclude=set(), memo={}) -> bool:
    # Check if current exclusion list in memo, and return that value if so
    key = tuple(exclude)
    if key in memo: return memo[key]

    # Return true if the sum of numbers in the list are equal to the target
    current_sum = sum([val for val in nums if val not in exclude])
    if current_sum == target: return True

    # Return true if any of the sub-sums are true
    for val in nums:
        if val not in exclude:
            next_exclude = exclude.union({val})
            memo[tuple(next_exclude)] = canSum(nums, target, next_exclude, memo)
            if memo[tuple(next_exclude)] is True: return True
    return False


# Naive function using the MUCH more intuitive idea from the video to subtract values from the target to try to reach 0.
def canSumSubtract(target: int, nums: List[int]) -> bool:
    if target == 0: return True
    elif target < 0: return False
    return any([canSumSubtract((target-val), nums) for val in nums])


# Addition of memos into this function
def canSumMemo(target: int, nums: List[int], memo={}) -> bool:
    if target in memo: return memo[target]
    if target == 0: return True
    elif target < 0: return False

    # memo[target] = any([canSumMemo((target-val), nums, memo) for val in nums])
    # NOTE: Shouldn't use comprehension here because it will finish the entire loop before returning True... inefficient

    # Loops through and returns true as soon as a true value is given
    for num in nums:
        # Don't need to assign to memo if true because we are exiting the parent function immediately
        if canSumMemo((target-num), nums, memo) == True: return True
    # If no true values given, set as false and return
    memo[target] = False
    return False


# First attempt to tabulate canSum
def canSumTab(target: int, nums: List[int]) -> bool:
    # Initialise table
    tab_len = target + 1
    tab = [False] * tab_len

    # Base cases
    tab[0] = True

    # Loop through
    for i in range(tab_len):
        # Return once we get to the target value
        if i == target: return tab[i]

        # If value is true, update downstream values
        if tab[i] == True:
            print(f"tab[{i}] = true")
            for num in nums:
                if (i+num) < tab_len:
                    tab[i+num] = True

nums = [5, 10]
target = 5
print(canSumTab(target, nums))
