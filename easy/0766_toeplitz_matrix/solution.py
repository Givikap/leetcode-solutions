class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            col = 0
            val = matrix[row][col]

            while row < rows and col < cols:
                if matrix[row][col] != val:
                    return False

                row += 1
                col += 1

        for col in range(1, cols):
            row = 0
            val = matrix[row][col]

            while row < rows and col < cols:
                if matrix[row][col] != val:
                    return False

                row += 1
                col += 1

        return True
