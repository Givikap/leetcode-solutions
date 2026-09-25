class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i, j = 0, 0

        while True:
            if matrix[i][j] == target:
                return True

            if i + 1 < len(matrix) and matrix[i + 1][j] <= target:
                i += 1
            elif j + 1 < len(matrix[0]):
                j += 1
            else:
                return False
