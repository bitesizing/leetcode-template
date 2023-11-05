"""https://leetcode.com/problems/binary-trees-with-factors/description/?envType=daily-question&envId=2023-10-26
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
"""
# %%
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        numset = set(arr)
        counts = {el:1 for el in arr}

        # start from smallest and calc number... recursive problem
        for product in arr:
            for factor1 in arr:
                if factor1 == product: break

                factor2 = product/factor1
                if not factor2.is_integer(): break
                factor2 = int(factor2)
                if factor2 in numset:
                    counts[product] += counts[factor1]*counts[factor2]*(1 if factor1==factor2 else 2)

        return sum(counts.values())

arr = [2,4,5,10]
print(Solution().numFactoredBinaryTrees(arr))
                
        

