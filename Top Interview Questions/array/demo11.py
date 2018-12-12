"""
Rotate Image

"""


class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for k in range(0, n - 1 - i):
                matrix[i][k], matrix[n - 1 - k][n - 1 - i] = matrix[n - 1 - k][n - 1 - i], matrix[i][k]
        print(matrix)
        for j in range(n):
            for k in range(n // 2):
                matrix[k][j], matrix[n - 1 - k][j] = matrix[n - 1 - k][j], matrix[k][j]



if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # matrix[::] = reversed(zip(*matrix))
    s.rotate(matrix)
    print(matrix)
