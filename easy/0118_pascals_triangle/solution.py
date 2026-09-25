class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        rows = []

        for r in range(num_rows):
            row = [1] * (r + 1)

            for i in range(1, r):
                row[i] = rows[-1][i - 1] + rows[-1][i]

            rows.append(row)

        return rows
