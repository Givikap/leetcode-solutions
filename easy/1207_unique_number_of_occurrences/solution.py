from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        return not any(
            count != 1 for count in Counter(Counter(arr).values()).values()
        )
