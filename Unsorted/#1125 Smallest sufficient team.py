"""https://leetcode.com/problems/smallest-sufficient-team/
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.
Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.
 - For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.
It is guaranteed an answer exists.
"""

from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
		n = len(req_skills)
		m = len(people)
		memo = {}
		s = {}
		for skill in req_skills: 
			s[skill] = set([idx_p for idx_p in range(m) if skill in people[idx_p]])

		def removePerson(ppl_set): 
			# Base cases
			ppl_tuple = tuple(ppl_set)
			if ppl_tuple in memo: return memo[ppl_tuple]
			if ppl_set == {}: return None
			for skill in s.values():
				if skill - ppl_set == skill: return None  # Return 'max' value possible if all people who know that skill have been removed

			return_set = ppl_set.copy()
			for current_p in ppl_set:
				new_set = removePerson({idx_p for idx_p in ppl_set if idx_p is not current_p})
				return_set = return_set if not new_set or len(new_set) > len(return_set) else new_set
			memo[ppl_tuple] = return_set
			return return_set
		
		people_set = {i for i in range(m)}
		result = list(removePerson(people_set))
		return result

	

req_skills = ["cpp", "python", "javascript", "kotlin", "ruby", "r", "c", "rust", "vb"]
people = [["cpp", "c", "rust"], ["cpp", "python", "javascript", "c", "r", "rust"], ["cpp", "python", "javascript", "c", "r", "vb"], ["cpp", "python", "javascript", "ruby", "kotlin", "r", "c", "rust", "vb"], ["cpp", "python", "javascript", "kotlin", "ruby", "r", "c", "rust", "vb"], ["python", "r"], ["cpp", "python", "javascript", "ruby", "kotlin", "r", "c", "rust", "vb"], ["cpp", "python", "javascript", "r", "c", "rust"], ["cpp", "javascript", "rust", "vb"], ["kotlin", "ruby", "c", "vb"], ["cpp", "python", "kotlin", "ruby", "rust", "vb"], ["ruby", "c", "r", "rust"], ["python", "javascript"], ["javascript", "ruby", "rust"], ["python", "javascript", "ruby", "c", "r", "rust", "vb"], ["cpp", "javascript", "kotlin", "r", "c", "vb"], ["c", "rust"], ["cpp", "kotlin", "ruby", "c", "r", "rust", "vb"], ["cpp", "python", "javascript", "ruby", "kotlin", "rust"], ["cpp", "javascript", "ruby"], ["vb"]]
print(Solution().smallestSufficientTeam(req_skills, people))