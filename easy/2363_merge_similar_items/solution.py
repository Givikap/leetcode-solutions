from collections import Counter


class Solution:
    def mergeSimilarItems(
        self, items1: list[list[int]], items2: list[list[int]]
    ) -> list[list[int]]:
        items_map = Counter()

        for value, weight in items1:
            items_map[value] += weight
        for value, weight in items2:
            items_map[value] += weight

        return sorted([value, weight] for value, weight in items_map.items())
