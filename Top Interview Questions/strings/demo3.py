"""
First Unique Character in a String

"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


if __name__ == '__main__':
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))
