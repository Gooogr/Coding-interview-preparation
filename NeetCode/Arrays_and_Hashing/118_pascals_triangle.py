# https://leetcode.com/problems/pascals-triangle/

from typing import List

# Zero-padding approach
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            tmp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(tmp[j] + tmp[j + 1])
            res.append(row)
        return res

# My solution with additional function
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def create_row(prev_row: List[int]):
            print(prev_row)
            if len(prev_row) == 1:
                return [1, 1]
            result = [1]
            for idx in range(len(prev_row) - 1):
                result.append(prev_row[idx] + prev_row[idx + 1])
            result.append(1)
            return result

        full_result = [[1]]
        if numRows == 1:
            return full_result
        else:
            for row_idx in range(numRows - 1):
                full_result.append(create_row(full_result[row_idx]))
        return full_result