#
#
# @param str string字符串 初始字符串
# @return string字符串
#
'''
链接：https://ac.nowcoder.com/acm/contest/6911/B
来源：牛客网

牛牛最近迷上了小游戏，于是他也想对他的01字符串进行一些操作，
01字符串上的0和0相邻时会变成1，
而1和1相邻时会在字符串上消失，
而0和1相邻时什么都不会发生，
牛牛现在把初始的字符串给你，
你能告诉牛牛这个字符串最后会变成什么样吗。

示例1
输入
复制
"00110001"
输出
复制
"01"
说明
00110001→1110001→10001→1101→01
备注:
字符串上的合并消失应优先与左边进行，例如000，中间的0优先与左边的0合并变为10，消失同理
 '''


class Solution:
    def solve(self, str):
        # write code here
        stack = [str[i] for i in range(len(str) - 1, -1, -1)]
        while stack:
            a = stack.pop()
            b = stack.pop()
            ans = ''
            if a == '0' and b == '0':
                ans = '1'
            elif a == '1' and b == '1':
                ans = ''
            
        
        return "".join(dp)
            


print(Solution().solve("00110001"))
