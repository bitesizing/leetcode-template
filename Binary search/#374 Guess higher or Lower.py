"""https://leetcode.com/problems/guess-number-higher-or-lower/
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
"""

class Solution:
	def __init__(self, pick=1):
		self.pick = pick

	def guess(self, num: int) -> int:
		""" Predefined 'guess' function that we are calling """
		if num < self.pick: return 1
		if num > self.pick: return -1
		return 0

	def guessNumber(self, n: int) -> int:
		# Probably just requires a binary tree...
		lo, hi, mid = 0, n, n//2
		current = self.guess(mid)

		while current != 0 and lo < hi:
			# Define vals
			mid = int((hi - lo) / 2) + lo  # General equation for midpoint with varying hi and lo

			if current == -1:  # If val > target then repeat with lower half of array
				hi = mid - 1  # NOTE: this can cause hi to be set to '-1' but it's fine because we never index hi at the end
			elif current == 1:  # Else repeat with upper half of array
				lo = mid + 1

			mid = (hi + lo) // 2
			current = self.guess(mid)
		return mid

print(Solution(4).guessNumber(10))
