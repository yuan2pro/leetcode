"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
]

"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        res = []
        prev = [1]
        res.append(prev)
        for idx in range(2, numRows + 1):
            prev = self.helper(prev, idx)
            res.append(prev)
        return res

    def helper(self, prev_row, idxRows):
        row_res = [1] * idxRows
        for i in range(1, idxRows - 1):
            row_res[i] = prev_row[i - 1] + prev_row[i]
        return row_res


if __name__ == '__main__':

    print(Solution().generate(5))
