import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        curr_i = 0
        min_cost = 0

        visited = {curr_i}
        heap = []

        while len(visited) != len(points):
            for i in range(len(points)):
                if i in visited:
                    continue

                heapq.heappush(
                    heap,
                    (
                        abs(points[curr_i][0] - points[i][0])
                        + abs(points[curr_i][1] - points[i][1]),
                        i,
                    ),
                )

            while heap:
                distance, other_i = heapq.heappop(heap)

                if other_i not in visited:
                    visited.add(other_i)
                    min_cost += distance
                    curr_i = other_i
                    break

        return min_cost
