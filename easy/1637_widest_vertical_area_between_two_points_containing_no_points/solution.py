class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()

        widestGap = 0

        for i in range(len(points) - 1):
            widestGap = max(widestGap, points[i + 1][0] - points[i][0])

        return widestGap
