class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)

        lucky_nums = []

        for row in range(rows):
            row_min = min(matrix[row])
            col = matrix[row].index(row_min)
            col_max = max(matrix[row][col] for row in range(rows))

            if row_min == col_max:
                lucky_nums.append(row_min)

        return lucky_nums
