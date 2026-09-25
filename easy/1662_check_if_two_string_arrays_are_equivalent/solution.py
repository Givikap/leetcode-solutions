class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return [c for tk in word1 for c in tk] == [
            c for tk in word2 for c in tk
        ]
