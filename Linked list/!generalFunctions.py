"""
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
        
class LinkedList:
    def convertToLinkedList(self, list_in, next_node=None):
        if not list_in: return next_node  # Base case
        return self.convertToLinkedList(list_in, ListNode(list_in.pop(), next_node))
    

list_in = [1, 2, 3, 4]
linked_list = LinkedList().convertToLinkedList(list_in)
a = 2