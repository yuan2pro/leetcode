class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#
# 返回牛牛能到达终点且不被淘汰的路径数
# @param n int整型
# @param Edge Point类一维数组
# @param f int整型一维数组
# @return int整型
#
# 7,[(7,2),(6,1),(5,2),(1,2),(4,6),(6,3)],[0,0,1,0,1,0,0]
# 4


class Solution:
    def solve(self, n, Edge: Point, f):
        ans = 0
        for i in range(n-1):
            if Edge[i].x == 1:

            elif Edge[i].y == 1:

                # write code here
