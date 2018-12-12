#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : demo_16.py
# @Author: ProYuan
# @Date  : 2018/12/6
# @Software : PyCharm
# @Desc  : 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)  # 行
        n = len(matrix[0])  # 列
        ans = []
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        while True:
            for j in range(left, right + 1):  # 从左至右
                ans.append(matrix[up][j])
            up += 1
            if up > down: break
            for i in range(up, down + 1):  # 从上往下
                ans.append(matrix[i][right])
            right -= 1
            if right < left: break
            for j in range(right, left - 1, -1):  # 从右往左
                ans.append(matrix[down][j])
            down -= 1
            if down < up: break
            for i in range(down, up - 1, -1):  # 从下往上
                ans.append(matrix[i][left])
            left += 1
            if left > right: break
        return ans


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(matrix))
