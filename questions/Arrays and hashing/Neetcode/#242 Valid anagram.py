"""https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise."""

from collections import Counter

class Solution:
	def isAnagram0(self, s: str, t: str) -> bool:
		""" Bog standard solution. Way faster than clever following solutions... >:( """
		s_arr = {}
		t_arr = {}

		for char in s:
			if char not in s_arr: s_arr[char] = 1
			else:s_arr[char] += 1

		for char in t:
			if char not in t_arr: t_arr[char] = 1
			else: t_arr[char] += 1
		return s_arr == t_arr

	def isAnagram1(self, s: str, t: str) -> bool:
		""" V readable solution using a homebrew 'counter' class... unfortunately quite slow! """
		class Counter:
			def __init__(self):
				self.counter = {}  # Initialise dictionary

			def add(self, char):
				if char not in self.counter: self.counter[char] = 1  # Assign to counter if char does not exist in it
				else: self.counter[char] += 1  # Increment if it does

		cs, ct = Counter(), Counter()
		[cs.add(char) for char in t]
		[ct.add(char) for char in s]
		return cs.counter == ct.counter

	def isAnagram2(self, s: str, t: str) -> bool:
		""" Ditches the counter class for a bog standard function. Still way slower than doing it manually! (without ref.ing a function) """
		def dict_add(dct, char):
			if char not in dct: dct[char] = 1  # Assign to counter if char does not exist in it
			else: dct[char] += 1  # Increment if it does

		count_s, count_t = {}, {}
		[dict_add(count_s, char) for char in t]
		[dict_add(count_t, char) for char in s]
		return count_s == count_t
	
	def isAnagram3(self, s: str, t: str) -> bool:
		""" Initialises one dict and tries to reduce it down to 0. Still slow!! """
		counter = {}

		for char in s:
			if char not in counter: counter[char] = 1  # Assign to counter if char does not exist in it
			else: counter[char] += 1  # Increment if it does

		for char in t:
			if char not in counter: return False
			elif counter.get(char) == 1: counter.pop(char)
			else: counter[char] -= 1

		return counter == {}

	def isAnagram4(self, s: str, t: str) -> bool:
		""" Uses the inbuilt python counters... """
		return Counter(s) == Counter(t)


# Solution
s, t = "aa", "a"
print(Solution().isAnagram4(s, t))
