"""
Reverse String

"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        l.reverse()
        return "".join(l)


if __name__ == '__main__':
    s = Solution()
    str =  "A man, a plan, a canal: Panama"
    print(s.reverseString(str))
