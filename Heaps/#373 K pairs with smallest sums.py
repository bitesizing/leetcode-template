"""https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
Given two arrays of ascending integers, define a pair consisting of one element from each array
Find the k pairs with the smallest sums
"""

from typing import List
from heapq import heappush, heappop

class Solution:
	def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
		# Can use a heap!
		result = []

		# Initialise our heap
		visited = set()
		heap = []
		heappush(heap, (nums1[0] + nums2[0], (0, 0)))  # Push sum (to be ordered in the heap), i & j

		# Main loop
		while heap and len(result) < k:
			_, popped = heappop(heap)
			i, j = popped[0], popped[1]
			result.append((nums1[i], nums2[j]))

			# Crucially, you push the right and down value from the one you popped!
			if i+1 < len(nums1) and (i+1, j) not in visited:
				heappush(heap, (nums1[i+1] + nums2[j], (i+1, j)))
				visited.add((i+1, j))
			if j+1 < len(nums2) and (i, j+1) not in visited:
				heappush(heap, (nums1[i] + nums2[j+1], (i, j+1)))
				visited.add((i, j+1))

		return result

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(Solution().kSmallestPairs(nums1, nums2, k))


