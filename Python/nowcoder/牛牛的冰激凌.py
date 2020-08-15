#
# 两个数表示答案
# @param n int整型 一次运输的冰激凌数量
# @param m int整型 总冰激凌数
# @param t int整型 一次运输的时间
# @param c int整型一维数组 表示每个冰激凌制作好时间<1e4
# @return int整型一维数组
#

# 2, 3, 10, [10, 30, 40]
# [50,2]
class Solution:
    def icecream(self, n, m, t, c):
        if m <= n:
            return [t, 1]
        
        # write code here
