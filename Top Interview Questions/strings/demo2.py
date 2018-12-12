"""
Reverse Integer
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = list(str(x))
        if s[0] == '-':
            s.reverse()
            s.remove('-')
            result = -(int("".join(s)))
        else:
            s.reverse()
            result = int("".join(s))
        if result > pow(2, 31) - 1 or result < -pow(2, 31):
            return 0
        else:
            return result


if __name__ == '__main__':
    x = -123
    s = Solution()
    print(s.reverse(x))
