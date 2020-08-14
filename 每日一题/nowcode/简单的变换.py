#
#
# @param n long长整型
# @return int整型
#
'''
链接：https://ac.nowcoder.com/acm/contest/6911/A
来源：牛客网

给你一个正整数n，重复进行以下操作：
1.如果n是奇数，令n=n-3n=n−3
2.如果n是偶数，令n=n/2n=n/2
重复上述直至n=0停止，请输出进行操作的次数，如果n永远无法变成零，输出-1

示例1
输入
复制
2
输出
复制
-1
说明
1:2->1(2/2=1)
2:1->-2(1-3=-2)
3:-2->-1((-2)/2=(-1))
4.-1->-4(-1-3=-4)
5.-4->-2((-4)/2=(-2))
6.-2->-1((-2)/2=(-1))
.......开始进入第三步操作到第五步操作的循环，n永远无法等于0，所以返回-1。
示例2
输入
复制
9
输出
复制
3
说明
1.9->6(9-3=6)
2.6->3(6/2=3)
3.3->0(3-3=0)
三步操作后n变为0，所以返回3。

'''


class Solution:
    def Numberofoperations(self, n):
        # write code here
        ans = 0
        dp = [1, 2, 4, 5, 8, 10]
        while n != 0:
            if n in dp:
                return -1
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 3
            ans += 1
        return ans


print(Solution().Numberofoperations(13))
