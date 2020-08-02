#
# 返回最少多少次操作后能使这几个数变成一个等差数列，如果完全不能构造成功，就返回-1
# @param n int整型 代表一共有n个数字
# @param b int整型一维数组 代表这n个数字的大小
# @return int整型
#
'''
链接：https://ac.nowcoder.com/acm/contest/6776/C
来源：牛客网

牛牛和牛妹在玩一个游戏，在他们面前有n个数，他们对每个数可以进行 +1 或 -1 操作，
但对于每一个数，该操作最多只能执行一次。
游戏胜利的目标是：使用最少的操作次数，将这几个数构造成一个等差数列。
牛牛特别想赢得游戏，所以他想让你帮他写一个程序，
得出最少多少次操作后能使这几个数变成一个等差数列，当然，如果完全不能构造成功，就输出-1。
'''
'''
输入:4,[24,21,14,10]
输出:3
说明:
在第一个例子中，牛牛应该对第一个数字+1，
对第二个数字-1，对第三个数字+1，而第四个数字应该保持不变。
最后，序列就变成了[25,20,15,10]，这是一个等差数列且操作次数最少。
'''


class Solution:
    def solve(self, n, b):
        if n <= 2:
            return 0
        l = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = b[0] + i
                y = b[1] + j
                z = y - x  # 等差
                ans = 0
                if i != 0:
                    ans += 1
                if j != 0:
                    ans += 1
                for k in range(2, n):
                    # y的下一个
                    xx = y + z
                    if abs(xx-b[k]) > 1:
                        break
                    else:
                        if xx - b[k] != 0:
                            ans += 1
                        y = xx
                    if k == n - 1:
                        l.append(ans)
        if len(l) == 0:
            return - 1
        else:
            return min(l)


c = [24, 21, 14, 10]
b = c
a = Solution().solve(4, b)  # 3
print(a)
# write code here
