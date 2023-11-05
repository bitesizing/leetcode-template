"""https://leetcode.com/problems/single-number-ii/
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List
import math

class SolutionI:
	""" Flexible solution with general functions, using ternary modulus; not optimised for leetcode speed. """

	def pop_sign(self, n):
		""" Returns the sign and abs val of n. 0 is treated as positive. """
		sign = int(math.copysign(1, n))
		abs_val = abs(n)
		return sign, abs_val

	def convertToBaseN(self, dec_num, base, digits=1, include_sign=True):
		""" Returns an array, converting an inputted decimal number into a base of your choice...
		The LAST bit is the signed int"""

		# Checks and exceptions
		if base <= 1: raise Exception("Sorry, no bases below two!")
		if digits < 1: raise Exception("At least one digit is needed!")

		# Pop sign and store for usage
		sign, dec_num = self.pop_sign(dec_num)

		# Handle special 0 case, then other cases
		if dec_num == 0:
			res = [0]*digits  # Make sure we always return at least one digit
		else:
			# If digits not set, dynamically figure it out based on size of input num
			if digits <= 1: digits = math.floor(math.log(dec_num, base)) + 1

			# Assign empty array of 0s, plus sign
			res = [0]*digits
			while dec_num > 0:
				current_digit = math.floor(math.log(dec_num, base))  # Find highest digit smaller than number, subtract from digits for asc. order
				res[digits-current_digit-1] += 1  # Increment value of that digit
				dec_num -= base**current_digit  # Base**current_digit is the 'magnitude' of that digit... ones, tens etc. in decimal

		#print(f"res+sign={res+[sign]}")
		return res + [sign] if include_sign else res  # Add sign on if include sign set to true

	def convertFromBaseN(self, num, base):
		"""Converts an array to a normal ass decimal int..."""
		return sum([num[-1-i]*(base**i) for i in range(len(num))])  # Base**i is the magnitude of that digit, then multiply by value

	def singleNumber(self, nums: List[int]) -> int:
		# Figure out the maximum number of digits needed (for the largest number)
		max_digits = math.floor(math.log(max([abs(num) for num in nums]), 3)) + 1
		ans = [0]*(max_digits+1)  # Extra bit to account for the sign

		# Main loop
		for num in nums:
			ternary_num = self.convertToBaseN(num, 3, max_digits)
			ans = [ans[i] + ternary_num[i] for i in range(max_digits+1)]
		ans = [i%3 for i in ans]  # Mod each digit of the answer by 3
		sign = 1 if ans.pop() == 1 else -1
		ans = self.convertFromBaseN(ans, 3)
		return ans*sign

nums = [0,1,0,1,0,1,99]
print(SolutionI().singleNumber(nums))

class SolutionII:
	""" Optimised solution for leetcode using bitwise operations. """
	def singleNumber(self, nums: List[int]) -> int:
		ans = 0  # Keeping track of the sign: 0 is positive and 1 is negative

		# Main loop through each bit of the binary representation of the number
		for i in range(32):  # For each specified bit
			bit_sum = 0
			for num in nums:
				bit_sum += (num >> i) & 1  # Rightshift the number so the least sig. bit is in the 1s column, then compare to 1.
			bit_sum %= 3  # Mod the bit_sum by 3... Any 'remainders' represent a unique bit
			ans += (bit_sum<<i)  # Leftshift by i and add this result to answer.

		# If the leftmost bit of the ans is 1 (aka if it is a negative number in two's complement), subtract 2**32 to convert into negative
		if (ans >> (31)) & 1 == 1: ans -= 2**32
		return ans

nums = [-2,-2,1,1,4,1,4,-5,4,-2]
a = SolutionII().singleNumber(nums)
print(a)

