from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        frequencyMap = defaultdict(int)
        for c in s:
            frequencyMap[c] += 1

        return "".join(
            c * frequency
            for c, frequency in sorted(
                frequencyMap.items(), key=lambda item: -item[1]
            )
        )
