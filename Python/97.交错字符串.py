#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                k = i + j - 1
                if i > 0:
                    dp[i][j] |= (dp[i-1][j] and s1[i-1] == s3[k])
                if j > 0:
                    dp[i][j] |= (dp[i][j-1] and s2[j-1] == s3[k])
        
        return dp[-1][-1]


# s1 = "a"
# s2 = ""
# s3 = "a"
# print(Solution().isInterleave(s1, s2, s3))
# @lc code=end
