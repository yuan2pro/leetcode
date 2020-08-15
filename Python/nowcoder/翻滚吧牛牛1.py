#
#
# @param k int整型 翻滚次数
# @return double浮点型
#
'''
链接：https://ac.nowcoder.com/acm/contest/6776/A
来源：牛客网

牛牛有一个边长为1的正六边形，只要牛牛一推它就可以一直滚下去，
正六边形左下角为A，牛牛想知道正六边形翻滚k次A点的轨迹边长是多少呢。
如图是正六边形翻滚一次的情况。给定正六边形翻滚次数k，求A点翻滚轨迹长度
'''
import math


class Solution:
    def circumference(self, k):
        p = math.pi
        l = [p / 3, 3 ** 0.5 * p / 3, 2 * p / 3, 3 ** 0.5 * p / 3, p / 3, 0]
        a = k // 6
        b = k % 6
        ans = a*sum(l)
        for i in range(b):
            ans += l[i]
        return ans
        # write code here