class Solution:
    def findRotation(
        self, matrix: list[list[int]], target: list[list[int]]
    ) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for _ in range(4):
            rotated_matrix = [[0] * cols for _ in range(rows)]

            for row in range(rows):
                for col in range(cols):
                    rotated_matrix[row][col] = matrix[col][row]

            for row in range(rows):
                rotated_matrix[row] = rotated_matrix[row][::-1]

            if rotated_matrix == target:
                return True

            matrix = rotated_matrix

        return False
