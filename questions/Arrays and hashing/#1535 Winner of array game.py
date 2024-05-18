"""Given an integer array arr of distinct integers and an integer k
A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
Return the integer which will win the game.
It is guaranteed that there will be a winner of the game."""

# %%
from typing import List
from collections import deque, defaultdict
from itertools import count
from heapq import heappush, heappop, heapify, heappushpop

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n == 1: return arr[0]  # base case if arr. has one item
        if k >= n-1: return max(arr)  # biggest always wins if whole arr is used
        current_max = max(arr[0], arr[1])
        current_points = 1

        # Loop through remaining items and calc how many wins.
        for item in arr[2:]:
            if current_points == k: return current_max
            if item > current_max:
                current_points = 1  # reset points
                current_max = item
            else:
                current_points += 1

        # If no item has won after first iteration, biggest item will always win, so return.
        return current_max


arr = [1, 2]
k = 2
print(Solution().getWinner(arr, k))