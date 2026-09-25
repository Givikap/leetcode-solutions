class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        firsts_map = {}
        lasts_map = {}

        for i, j in zip(range(len(colors)), range(len(colors) - 1, -1, -1)):
            if colors[i] not in firsts_map:
                firsts_map[colors[i]] = i
            if colors[j] not in lasts_map:
                lasts_map[colors[j]] = j

        max_distance = 1

        for i in firsts_map.values():
            for j in lasts_map.values():
                if colors[i] != colors[j]:
                    max_distance = max(max_distance, abs(i - j))

        return max_distance
