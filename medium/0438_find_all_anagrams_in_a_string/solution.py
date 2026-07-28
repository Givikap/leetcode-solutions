from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        k = len(p)

        sCharCounter = [0] * 26
        pCharCounter = [0] * 26

        for i in range(k):
            sCharCounter[ord(s[i]) - 97] += 1
            pCharCounter[ord(p[i]) - 97] += 1

        substrings = []
        if sCharCounter == pCharCounter:
            substrings.append(0)

        for i in range(len(s) - k):
            sCharCounter[ord(s[i]) - 97] -= 1
            sCharCounter[ord(s[i + k]) - 97] += 1

            if sCharCounter == pCharCounter:
                substrings.append(i + 1)

        return substrings
