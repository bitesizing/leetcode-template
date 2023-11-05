"""https://leetcode.com/problems/find-eventual-safe-states/
There is a directed graph of n nodes with each node labeled from 0 to n - 1, represented by a 2D int array where graph[i] is an int. array of nodes adjacent to node i.
- A 'terminal' node contains no outgoing edges.
- A 'safe' node has every possible path leading to a terminal node, or other safe nodes.
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""

from typing import List

class Solution:
	def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
		""" Dynamic programming approach finding 'safe' paths (ending in terminal nodes), keeping track of which nodes are visited. """
		# Initialise external vars
		n = len(graph)
		visited = [None]*n

		def isSafe(idx: int) -> bool:
			# We only need to visit each node ONCE, so check this and update visited
			if visited[idx] is not None: return visited[idx]
			visited[idx] = False

			for neighbour in graph[idx]:
				if visited[neighbour] == False or isSafe(neighbour) == False: return False  # Return FALSE if unsafe (recursively)

			visited[idx] = True  # If NO NEIGHBOURS (i.e. terinal node) or all neighbours safe, update visited[idx] and return
			return True
		
		return [node for node in range(n) if isSafe(node)]


graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(Solution().eventualSafeNodes(graph))


