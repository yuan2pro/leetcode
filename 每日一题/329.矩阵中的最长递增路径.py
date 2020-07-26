#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0

        @lru_cache(maxsize=None)    # 注意这里的LRU缓存，要设置为不限制缓存大小
        def _dfs(i, j):
            best = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, _dfs(ni, nj) + 1)
            return best

        rows, cols = len(matrix), len(matrix[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, _dfs(i, j))
        return ans
# @lc code=end

