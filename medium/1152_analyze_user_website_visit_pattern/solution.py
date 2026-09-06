from collections import Counter, defaultdict
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        visitsMap = defaultdict(list)

        for _, u, w in sorted(zip(timestamp, username, website)):
            visitsMap[u].append(w)

        patternsCounter = Counter()

        for visits in visitsMap.values():
            for pattern in set(combinations(visits, 3)):
                patternsCounter[pattern] -= 1

        return list(
            min(
                patternsCounter,
                key=lambda pattern: (patternsCounter[pattern], pattern),
            )
        )
