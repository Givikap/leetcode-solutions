from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = defaultdict(list)

        for s in strs:
            anagramsMap[tuple(sorted(s))].append(s)

        return list(anagramsMap.values())
