class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 0

        time = 0

        x1, y1 = points.pop()

        while points:
            x2, y2 = points.pop()
            time += max(max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2))
            x1, y1 = x2, y2

        return time
