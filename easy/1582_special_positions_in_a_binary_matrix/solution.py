class Solution:
    def numSpecial(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        row_sums = [0] * rows
        col_sums = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    row_sums[row] += matrix[row][col]
                    col_sums[col] += matrix[row][col]

        count = 0

        for row in range(rows):
            if row_sums[row] == 1:
                for col in range(cols):
                    if col_sums[col] == 1 and matrix[row][col] == 1:
                        count += 1

        return count
