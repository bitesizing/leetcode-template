"""https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.queue = deque()     

    def get(self, key: int) -> int:
        if self.cache.get(key):
            self.cache[key] = (self.cache.get(key)[0], self.count)
            self.queue.append((key, self.count))
            self.count += 1
        print(self.cache.get(key, [-1])[0])
        return self.cache.get(key, [-1])[0]    

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            curr_key, queue_count = self.queue.popleft()
            while queue_count != self.cache[curr_key][1]:
                curr_key, queue_count = self.queue.popleft()
            del self.cache[curr_key]

        self.cache[key] = (value, self.count)
        self.queue.append((key, self.count))  # Append keys to queue...
        self.count += 1

class LRUCache:
    """ Modified function capitalising off the fact that python dictionaries are ordered. """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if self.cache.get(key): self.cache[key] = self.cache.pop(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache: del self.cache[key]
        elif len(self.cache) == self.capacity: del self.cache[next(iter(self.cache))]
        self.cache[key] = value

cache = LRUCache(2)
cache.get(2)
cache.put(2,6)
cache.get(1)
cache.put(1,5)
cache.put(1,2)
cache.get(1)
cache.get(2)
a = 2
