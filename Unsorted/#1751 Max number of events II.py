"""https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
Return the maximum sum of values that you can receive by attending events.
"""

from typing import List
import math
from collections import deque, defaultdict

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        return
	

events = [[1,2,4],[3,4,3],[2,3,1]]
k = 2
print(Solution().maxValue(events, k))