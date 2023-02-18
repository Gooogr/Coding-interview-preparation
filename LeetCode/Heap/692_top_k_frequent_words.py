# https://leetcode.com/problems/top-k-frequent-words/

import heapq
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_map = {}
        for word in words:
            count_map[word] = count_map.get(word, 0) + 1
        pairs = [(-freq, word) for word, freq in count_map.items()]
        heapq.heapify(pairs)
        result = []
        while len(result) < k:
            _, word = heapq.heappop(pairs)
            result.append(word)
        return result