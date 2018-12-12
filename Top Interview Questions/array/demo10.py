"""
Valid Sudoku

"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        Cell = [[] for i in range(9)]
        Col = [[] for i in range(9)]
        Row = [[] for i in range(9)]
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    k = (i // 3) * 3 + j // 3  # 5//2=2
                    if num in Cell[k] or num in Col[j] or num in Row[i]:
                        return False
                    Cell[k].append(num)
                    Col[j].append(num)
                    Row[i].append(num)
        print(Cell)
        print(Col)
        print(Row)
        return True


if __name__ == '__main__':
    s = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(s.isValidSudoku(board))
