#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len1, len2 = len(p), len(s)
        dp = [[False]*(len2+1) for _ in range(len1+1)]
        dp[0][0] = True
        for i in range(1, len1+1):
            if p[i - 1] != '*':
                break
            dp[i][0] = True

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
        return dp[-1][-1]


# @lc code=end
