#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        dp = [False for _ in range(len(s))]
        index = 0
        for i in range(len(s)):
            for j in range(index, len(t)):
                if s[i] == t[j]:
                    dp[i]=True
                    index=j+1
                    break
                elif j == len(t) - 1:
                    return False
        return dp[-1]


# @lc code=end
