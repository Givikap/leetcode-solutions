class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for row in range(len(matrix) - 1):
            for col in range(row + 1, len(matrix)):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col],
                )

        for row in range(len(matrix)):
            for col in range(len(matrix) // 2):
                matrix[row][col], matrix[row][-col - 1] = (
                    matrix[row][-col - 1],
                    matrix[row][col],
                )
