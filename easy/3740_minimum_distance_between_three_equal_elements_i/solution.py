from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        indices_map = defaultdict(list)

        for i, num in enumerate(nums):
            indices_map[num].append(i)

        min_dist = float("inf")

        for indices in indices_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    min_dist = min(min_dist, 2 * (indices[i + 2] - indices[i]))

        return min_dist if min_dist != float("inf") else -1
