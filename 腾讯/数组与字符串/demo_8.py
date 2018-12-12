# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 11:51
# @Author  : ProYuan
"""
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        l = []
        for x in s:
            if x == "(" or x == "{" or x == "[":
                l.append(x)
            else:
                if not l:
                    return False
                else:
                    s = l.pop()
                    if x == ")" and s == "(":
                        continue
                    elif x == "}" and s == "{":
                        continue
                    elif x == "]" and s == "[":
                        continue
                    else:
                        return False
        if not l:
            return True
        return False

    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapper = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in mapper.values():
                stack.append(char)
            elif stack == [] or stack.pop() != mapper[char]:
                return False

        return not stack


if __name__ == '__main__':
    print(Solution().isValid(s=""))
