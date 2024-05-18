"""https://leetcode.com/problems/group-anagrams/description/
Given an array of strings strs, group the anagrams together. You can return the answer in any order."""

from collections import Counter
from typing import List

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		string_dict = {}

		for string in strs:
			counted_string = Counter(string)
			if counted_string in string_dict: string_dict[counted_string].append(string)
			else: string_dict[counted_string] = [string]
		return [val for val in string_dict]

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
