#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        h, w = len(board), len(board[0])

        def backtrack(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = di + i, dj + j
                if 0 <= newi < h and 0 <= newj < w:
                    if (newi, newj) not in visited:
                        if backtrack(newi, newj, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        visited = set()
        for i in range(h):
            for j in range(w):
                if backtrack(i, j, 0):
                    return True
        return False

# @lc code=end
