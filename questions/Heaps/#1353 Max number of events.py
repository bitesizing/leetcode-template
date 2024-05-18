"""https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
Return the maximum number of events you can attend.
"""

from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
	def maxEvents(self, events: List[List[int]]) -> int:
		n = len(events)
		events.sort()  # Sort based on start_day (needed!), end_day (minimises swaps in the heap?)
		end_heap = []  # Min heap sorting all events that have started based on end_day

		event = n_attended = 0
		current_day = events[0][0]
		while True:
			if event >= n and end_heap == []: break
			while event < n and events[event][0] == current_day:
				heappush(end_heap, events[event][1])  # Push all valid end_days to min_heap
				event += 1
			while end_heap and end_heap[0] < current_day: heappop(end_heap)  # Pop all expired events
			if end_heap:
				heappop(end_heap)
				n_attended += 1
			if not end_heap and event<n: current_day = events[event][0]  # Set current day to start of next event not yet added if end heap is empty
			else: current_day += 1
		return n_attended
	

	def maxEvents2(self, events: List[List[int]]) -> int:
		""" Solution imported from leetcode that does better than mine, but I can't tell why... """
		n = len(events)
		events.sort()
		end_heap = []

		event = n_attended = 0
		curr_day = events[0][0]  # DIFFERENT
		while event<n:  # DIFFERENT
			# SAME 
			while event<n and events[event][0]==curr_day:
				heappush(end_heap, events[event][1])
				event += 1

			# Attend started event that ends earliest
			heappop(end_heap)
			n_attended += 1
			curr_day += 1
			
			# Remove all expired events
			while end_heap and end_heap[0]<curr_day: heappop(end_heap)
			# If no started events left, move to the next startDay
			if event<n and not end_heap: curr_day = events[event][0]

		# Events that started that are still left in heap
		while end_heap:
			# Non-expired started event that ends earliest
			if heappop(end_heap)>=curr_day:
				curr_day += 1
				n_attended += 1

		return n_attended



	
events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
print(Solution().maxEvents(events))