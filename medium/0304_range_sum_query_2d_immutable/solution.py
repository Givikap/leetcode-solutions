class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix_sums_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                self.prefix_sums_matrix[row][col] = (
                    matrix[row - 1][col - 1]
                    + self.prefix_sums_matrix[row - 1][col]
                    + self.prefix_sums_matrix[row][col - 1]
                    - self.prefix_sums_matrix[row - 1][col - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix_sums_matrix[row2 + 1][col2 + 1]
            - self.prefix_sums_matrix[row2 + 1][col1]
            - self.prefix_sums_matrix[row1][col2 + 1]
            + self.prefix_sums_matrix[row1][col1]
        )
