#
# 返回重新分配后，满足牛牛要求的水量的瓶子最多的数量
# @param n int整型 瓶子的数量
# @param x int整型 牛牛的对瓶中的水量要求
# @param a int整型一维数组 每个瓶子中的含水量
# @return int整型
#
'''
在牛牛面前有n个瓶子，每个瓶子的大小体积都一样，但是每个瓶子内的含水量都不相同。
因为牛牛是个完美主义者，他希望瓶子中的水能够满足他的要求，
他的要求是瓶子中的水最少为x。所以他打算对这些瓶子里的水进行重新分配，
以满足最多的瓶子中水量大于等于x。
牛牛的分配规则是：每次可以选择多个瓶子，将里面的水平均分配到已选择的瓶子中。
给定n个瓶子和牛牛的对瓶中的水量要求x，以及n个瓶子中的含水量，
求最多可以有多少个瓶子满足牛牛的要求？
'''


class Solution:
    def solve(self, n, x, a):
        ans = 0
        a.sort(reverse=True)
        t = 0
        for i in range(len(a)):
            t += a[i]
            if t / (i + 1) > x:
                ans += 1
        return ans


print(Solution().solve(2, 5, [4,3]))
# write code here
