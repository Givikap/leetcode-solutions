class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        cols = len(grid[0])

        negatives_count = 0

        for row in grid:
            left = 0
            right = cols - 1

            while left <= right:
                mid = left + (right - left) // 2

                if row[mid] < 0 and (mid == 0 or row[mid - 1] >= 0):
                    negatives_count += cols - mid
                    break
                elif row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1

        return negatives_count
