#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if x == ')':
                   if a != '(':
                       return False
                elif x == '}':
                    if a!='{':
                        return False
                elif x == ']':
                    if a!='[':
                        return False
        if not stack:
            return True
        else:
            return False
        

# @lc code=end

