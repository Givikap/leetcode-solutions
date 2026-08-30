from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort()

        sequences = [s]
        explored = set()

        while sequences:
            sequence = sequences.pop()

            if len(sequence) == 0:
                return True

            if sequence in explored:
                continue
            explored.add(sequence)

            for word in wordDict:
                if sequence.endswith(word):
                    sequences.append(sequence[: len(sequence) - len(word)])

        return False
