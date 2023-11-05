"""https://leetcode.com/problems/put-marbles-in-bags/
Given an array of marble weights, divide the marbles into k bags using the following rules:
	No bag is empty.
	If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
	The cost of a bag containing marbles i to j = weights[i] + weights[j]
The score after distributing the marbles is the sum of the costs of all the k bags.
Return the difference between the maximum and minimum scores among marble distributions.
"""

from typing import List
import heapq

class Solution:
	def putMarbles(self, weights: List[int], k: int) -> int:
		min_heap, max_heap = [], []
		for i in range(len(weights)-1):
			consec_sum = weights[i] + weights[i+1]  # Count consecutive sums
			if i < k-1:
				heapq.heappush(min_heap,  consec_sum)
				heapq.heappush(max_heap, -consec_sum)  # Push negative values to make a max heap
			else:
				heapq.heappushpop(min_heap,  consec_sum)
				heapq.heappushpop(max_heap, -consec_sum)
		return(sum(min_heap+max_heap))  # Add two together bc one has negative values (double negative)

weights = [1,3,5,1]
k = 2
print(Solution().putMarbles(weights, k))