import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [(x * x + y * y, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(heap)

        return [points[heapq.heappop(heap)[1]] for _ in range(k)]
