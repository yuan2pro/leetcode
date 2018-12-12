"""
Valid Anagram

"""

import collections


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        if sl == tl:
            return True
        else:
            return False

    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)


if __name__ == '__main__':
    s = "rat"
    t = "car"
    print(Solution().isAnagram1(s, t))
