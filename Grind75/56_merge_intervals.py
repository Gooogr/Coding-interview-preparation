# https://leetcode.com/problems/merge-intervals
from typing import List

# O(n*log(n))
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        for start_idx, end_idx in intervals[1:]:
            last_end_idx = result[-1][1]
            if start_idx <= last_end_idx: # if intervals intersect
                result[-1][1] = max(last_end_idx, end_idx)  # max() to handle situations like [[1, 5], [2, 4]]
            else:
                result.append([start_idx, end_idx])
        return result