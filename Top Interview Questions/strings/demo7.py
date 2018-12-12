"""
Implement strStr()

"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle != " ":
            if needle in haystack:
                return haystack.index(needle)
            elif needle not in haystack:
                return -1
        else:
            return 0


if __name__ == '__main__':
    haystack = "hello"
    needle = ""
    print(Solution().strStr(haystack, needle))
