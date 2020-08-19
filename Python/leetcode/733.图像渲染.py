#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        old_color = image[sr][sc]

        def dfs(r, c):
            nonlocal row, col, old_color, newColor
            if r < 0 or c < 0 or r > row - 1 or c > col - 1 or image[r][c] != old_color or image[r][c] == newColor:
                return
            image[r][c] = newColor

            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        dfs(sr, sc)
        return image


# @lc code=end
