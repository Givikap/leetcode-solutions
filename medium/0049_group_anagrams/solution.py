from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramsMap = defaultdict(list)

        for s in strs:
            anagramsMap[tuple(sorted(s))].append(s)

        return list(anagramsMap.values())
