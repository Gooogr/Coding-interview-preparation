# https://leetcode.com/problems/last-stone-weight

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # trivial case
        if len(stones) < 2:
            return stones[0]
        # inverted weights, because heapq is minheap
        arr = [-item for item in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            first_stone = heapq.heappop(arr)
            second_stone = heapq.heappop(arr)
            if first_stone != second_stone: 
                heapq.heappush(arr, first_stone - second_stone)

        # in case all stones collapsed
        arr.append(0)
        return arr[0] * -1