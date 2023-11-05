"""https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false."""

from typing import List

class Solution:
	""" LOGIC: If you have find a loop, return false. If there are no loops (i.e. if all nodes are 'safe', then return true.)"""

	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		""" Dynamic programming approach finding 'safe' paths (ending in terminal nodes), keeping track of which nodes are visited. """
		# Initialise external vars
		graph = [[] for i in range(numCourses)]
		visited = [None]*numCourses

		def isSafe(idx: int) -> bool:
			# We only need to visit each node ONCE, so check this and update visited
			if visited[idx] is not None: return visited[idx]
			visited[idx] = False

			for neighbour in graph[idx]:
				if visited[neighbour] == False or isSafe(neighbour) == False: return False  # Return FALSE if unsafe (recursively)
			visited[idx] = True  # If NO NEIGHBOURS (i.e. terinal node) or all neighbours safe, update visited[idx] and return
			return True
		
		# Build graph
		for pair in prerequisites: graph[pair[1]].append(pair[0])
		for node in range(numCourses): 
			if isSafe(node) == False: return False
		return True


numCourses = 2
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses, 	prerequisites))