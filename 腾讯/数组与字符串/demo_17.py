#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : demo_17.py
# @Author: ProYuan
# @Date  : 2018/12/6 14:46
# @Software : PyCharm
# @Desc  :

"""
螺旋矩阵 II
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
import numpy as np


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        total = n ** 2
        l = [i for i in range(1, total + 1)]
        ans = np.zeros((n, n), dtype=np.int)
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        a = 0
        while True:
            for i in range(left, right + 1):  # 从左至右
                ans[left, i] = l[a]
                a += 1
            up += 1
            if up > down: break
            for j in range(up, down + 1):
                ans[j, right] = l[a]
                a += 1
            right -= 1
            if right < left: break
            for i in range(right, left - 1, -1):
                ans[down, i] = l[a]
                a += 1
            down -= 1
            if down < up: break
            for j in range(down, up - 1, -1):
                ans[j, left] = l[a]
                a += 1
            left += 1
            if left > right: break
        return ans.tolist()

    def generateMatrix1(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        M = [[0 for _ in range(n)] for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for c in range(1, n * n + 1):
            M[i][j] = c
            if M[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i, j = i + di, j + dj
        return M


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
