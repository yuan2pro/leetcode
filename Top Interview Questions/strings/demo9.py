"""
Longest Common Prefix

"""

import collections


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)

        s1 = strs[0]
        s2 = strs[-1]

        prefix = ""
        for index in range(min(len(s1), len(s2))):
            if s1[index] == s2[index]:
                prefix += s1[index]
            else:
                break

        return prefix

    class Solution:
        def longestCommonPrefix2(self, strs):
            if len(strs) == 0:
                return ''
            for i in range(len(strs[0])):
                letter = strs[0][i]
                for string in strs:
                    if len(string) <= i or string[i] != letter:
                        return strs[0][:i]

            return strs[0]


if __name__ == '__main__':
    strs =  ["flower","flow","flight"]
    print(Solution().longestCommonPrefix1(strs))
