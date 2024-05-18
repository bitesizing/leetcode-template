"""https://leetcode.com/problems/add-two-numbers-ii/

"""

from typing import List, Optional
import math
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
			if l1.val == 0 and l2.val == 0: return ListNode(0, None)
			def convertToInt(linked_list: Optional[ListNode]) -> int:
				""""""
				result = 0
				while linked_list:
					result *= 10
					result += linked_list.val
					linked_list = linked_list.next
				return result
			i_sum = convertToInt(l1) + convertToInt(l2)

			# Feed back into linked list
			def generateLinkedList(i_sum: int, next_node: Optional[ListNode]):
				if i_sum == 0: return next_node  # Base case
				return generateLinkedList(i_sum//10, ListNode(i_sum%10, next_node))
			return generateLinkedList(i_sum, None)
	
	
l1 = [7,2,4,3]
l2 = [5,6,4]
print(Solution().addTwoNumbers)