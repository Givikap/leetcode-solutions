from utils.python import UnionFind


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        uf = UnionFind(n + 1)

        for a, b, _ in roads:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)

        minDistance = float("inf")

        for a, _, distance in roads:
            if uf.find(1) == uf.find(a):
                minDistance = min(minDistance, distance)

        return minDistance
