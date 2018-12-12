"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) == 1:
            return False
        l = []
        for x in s:
            if x == "(" or x == "{" or x == "[":
                l.append(x)
            if len(l) == 0:
                return False
            elif x == ")":
                if l.pop() != "(":
                    return False
            elif x == "}":
                if l.pop() != "{":
                    return False
            elif x == "]":
                if l.pop() != "[":
                    return False
        if not l:
            return True
        else:
            return False


if __name__ == '__main__':
    s =  "()"
    print(Solution().isValid(s))
