#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(board, x, y):
            cnt = 0
            for i in range(8):
                m = x + dx[i]
                n = y + dy[i]
                if n < 0 or m < 0 or m >= len(board) or n >= len(board[0]):
                    continue
                if board[m][n] == 'M':
                    cnt += 1
            if cnt > 0:
                board[x][y] = chr(cnt + ord('0'))
                return
            board[x][y] = 'B'
            for i in range(8):
                m = x + dx[i]
                n = y + dy[i]
                if n < 0 or m < 0 or m >= len(board) or n >= len(board[0]) or board[m][n] != 'E':
                    continue
                dfs(board, m, n)
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        x = click[0]
        y = click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(board, x, y)
        return board


# @lc code=end
