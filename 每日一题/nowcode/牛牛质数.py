#
# 返回两个区间内各取一个值相乘是p的倍数的个数
# @param a int整型 第一个区间的左边界
# @param b int整型 第一个区间的右边界
# @param c int整型 第二个区间的左边界
# @param d int整型 第二个区间的右边界
# @param p int整型 质数
# @return long长整型
#

'''
链接：https://ac.nowcoder.com/acm/contest/6914/B
来源：牛客网
'''


class Solution:
    def numbers(self, a, b, c, d, p):
        # write code here
        ab = b - a + 1
        cd = d - c + 1
        cnt1 = b // p - (a - 1) // p
        cnt2 = d // p - (c - 1) // p
        return ab * cnt2 + cd * cnt1 - cnt1 * cnt2


print(Solution().numbers(3, 7, 4, 6, 3))
