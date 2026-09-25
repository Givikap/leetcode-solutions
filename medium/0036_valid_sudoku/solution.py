class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowsMap = [[False] * 9 for _ in range(9)]
        colsMap = [[False] * 9 for _ in range(9)]
        boxesMap = [[False] * 9 for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                di = ord(board[row][col]) - 49
                if rowsMap[row][di] or colsMap[col][di]:
                    return False

                bi = 3 * (row // 3) + col // 3
                if boxesMap[bi][di]:
                    return False

                rowsMap[row][di] = True
                colsMap[col][di] = True
                boxesMap[bi][di] = True

        return True
