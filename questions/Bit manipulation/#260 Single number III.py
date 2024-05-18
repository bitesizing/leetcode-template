"""https://leetcode.com/problems/single-number-iii/
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
"""

from typing import List
import math

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		def calcAnswer(nums: List[int], bit_key=False) -> int:
			ans = 0

			# Main loop through each bit of the binary representation of the number
			for i in range(32):  # For each specified bit...
				bit_sum = 0
				for num in nums:
					# Bit_keys allow us to separate out two answers based on a key bit
					if (bit_key is False) or (num>>bit_key & 1 == 0):
						bit_sum += (num >> i) & 1  # Rightshift the number so the least sig. bit is in the 1s column, then compare to 1.
				bit_sum %= 2  # Mod the bit_sum by 3... Any 'remainders' represent a unique bit
				ans += (bit_sum<<i)  # Leftshift by i and add this result to answer.
			return ans

		ans_XOR = calcAnswer(nums)  # Calculate XOR
		rightmost_set = int(math.log2(ans_XOR&-ans_XOR))  # Equation to find the rightmost 'set' (==1) bit of a binary number

		ans = [calcAnswer(nums, rightmost_set)]
		ans.append(ans[0]^ans_XOR)  # XOR the first unique number with ans_XOR to get the second, then append
		ans = [(x-2**32) if (x>>31 & 1 == 1) else x for x in ans]  # If the leftmost bit == 1, subtract 2**32 to convert into negative
		return ans

nums = [-2, 0, -1, -1, 5]
ans = Solution().singleNumber(nums)
print(ans)

