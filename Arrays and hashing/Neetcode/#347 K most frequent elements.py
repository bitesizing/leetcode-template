"""https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List
import heapq

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		""" Function using hash-tables and min heaps to count """
		# Count the occurrences of each number
		counter = {}  # 'int' means when the defaultdict is queried for a value that is not present, it adds 0
		for num in nums: counter[num] = counter.get(num, 0) + 1

		# Iterate through our dict and check if each val is bigger than smallest value in array, using min_heaps
		top_k = []
		for key, value in counter.items():
			if len(top_k) < k: heapq.heappush(top_k, (value, key))  # Automatically push if top_k has not reached full size yet
			elif value > top_k[0][0]: heapq.heappushpop(top_k, (value, key))  # If current val > min val, replace min val
		return [k_tuple[1] for k_tuple in top_k]  # Return keys from tuples


	def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
		""" Similar but alt. approach using max_heaps. V similar speed, bit more readable """
		# Count the occurrences of each number
		counter = {}  # 'int' means when the defaultdict is queried for a value that is not present, it adds 0
		for num in nums: counter[num] = counter.get(num, 0) + 1

		# Convert counter to max heap, then pop first k values
		top_k = [(-value, key) for key, value in counter.items()]  # Taking the negative of the value means we can use min_heap as a max heap
		heapq.heapify(top_k)  # Turn the counter into a max_heap
		ans = []
		while len(ans) < k:
			ans.append(heapq.heappop(top_k)[1])
		return ans

nums = [5,3,1,1,1,3,73,1]
k = 2
print(Solution().topKFrequent2(nums, k))
