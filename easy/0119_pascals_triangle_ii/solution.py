class Solution:
    def getRow(self, row_index: int) -> list[int]:
        row = [1] * (row_index + 1)

        for r in range(2, row_index + 1):
            prev = row[0]

            for i in range(1, r):
                prev, row[i] = row[i], prev + row[i]

        return row
