'''
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，
可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''


class Solution:
    def trap(self, height) -> int:
        l = len(height)
        if l < 3:
            return 0
        ans = 0
        left_max_arr = [0] * l
        right_max_arr = [0] * l
        left_max_arr[0] = height[0]
        right_max_arr[l - 1] = height[l - 1]
        for i in range(1, l):
            left_max_arr[i] = max(left_max_arr[i - 1], height[i])
        for i in range(l - 2, -1, -1):
            right_max_arr[i] = max(right_max_arr[i + 1], height[i])
        for i in range(l):
            ans += min(left_max_arr[i], right_max_arr[i]) - height[i]
        return ans

