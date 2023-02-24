# https://leetcode.com/problems/task-scheduler/

from typing import List

# General idea:
# Input: AAABBB, n = 2

# A B idl
# A B idl
# A B

# freqs = [3, 3, 0, ..., 0]

# We need to sum two areas: rectangle + row
# rectangle area = (max_freq - 1) * (n + 1)
# row area = amount of max_freq elements

"""
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Count the number of tasks
        freqs = [0] * 26
        for task in tasks:
            freqs[ord(task) - ord('A')] += 1
        # Sort the tasks by their count
        freqs = sorted(freqs, reverse=True)
        max_freq = freqs[0]
        total_max_freqs = sum([freq == max_freq for freq in freqs])

        return max((max_freq - 1) * (n + 1) + total_max_freqs, 
                    len(tasks)) # if n = 0
