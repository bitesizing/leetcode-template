""" https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false.
He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question.
In addition, you are given an integer k, the maximum number of times you may perform the following operation:
Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
"""

class Solution:
	def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
		""" Standard sliding window approach, sliding through twice for "T" and "F" values. """
		n = len(answerKey)

		def calcMaxConsecutive(char):
			lo, max_consecutive, k_remaining = 0, 0, k  # k_remaining keeps track of the number of 'changes' we can make

			for hi in range(n):  # Iterate through right pointer
				if answerKey[hi] != char:
					k_remaining -= 1
					if k_remaining == -1:  # We can no longer be 'greedy' and expand right
						max_consecutive = max(max_consecutive, hi-lo)

				while k_remaining < 0:  # Increment left once there are too many incongruent values to change
					lo += 1
					if answerKey[lo-1] != char:
						k_remaining += 1
						if k_remaining == 0:  # Here is the leftmost legal position
							max_consecutive = max(max_consecutive, hi-lo+1)
			max_consecutive = max(max_consecutive, n - lo)
			return max_consecutive

		return max(calcMaxConsecutive("T"), calcMaxConsecutive("F"))

	def maxConsecutiveAnswers2(self, answerKey: str, k: int) -> int:
		""" Standard sliding window approach, sliding through twice for "T" and "F" values. """
		n = len(answerKey)

		f_changes = t_changes = f_lo = t_lo = max_consecutive = 0
		for hi in range(n):
			if answerKey[hi] == "T":
				t_changes -= 1
				if t_changes == -1: max_consecutive = max(max_consecutive, hi-t_lo)
			else:
				f_changes -= 1
				if f_changes == -1: max_consecutive = max(max_consecutive, hi-f_lo)

			while t_changes < 0:
				t_lo += 1
				if answerKey[t_lo-1] == "T":
					t_changes += 1
					if t_changes == 0: max_consecutive = max(max_consecutive, hi-t_lo + 1)

			while f_changes < 0:
				f_lo += 1
				if answerKey[f_lo-1] == "F":
					f_changes += 1
					if f_changes == 0: max_consecutive = max(max_consecutive, hi-f_lo + 1)
		max_consecutive = max(max_consecutive, n-t_lo, n-f_lo)
		return max_consecutive




answerKey = "TTFTTTTTFT"
k = 1
print(Solution().maxConsecutiveAnswers2(answerKey, k))
