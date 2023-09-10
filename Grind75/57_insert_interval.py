# https://leetcode.com/problems/insert-interval/
from typing import List

# Time complexity: O(n*log(n))
# Memory complexity: O(n)
# Add -> sort -> merge intervals (leetcode 56)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        for start, stop in intervals:
            last_end_idx = result[-1][1]
            if start <= last_end_idx:
                result[-1][1] = max(stop, last_end_idx)
            else:
                result.append([start, stop])
        return result
    

# Time complexity: O(n)
# Memory complexity: O(n)
# Neetcode approach
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # left side edgecase
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # rigth side edgecase
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # update newInterval with new merging borders
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                               max(newInterval[1], intervals[i][1])]
        # If we not exited above - exit here
        res.append(newInterval)
        return res


