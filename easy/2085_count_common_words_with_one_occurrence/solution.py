from collections import Counter


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        words1Counter = Counter(words1)

        wordsCount = 0

        for word, count in Counter(words2).items():
            if count == 1 and words1Counter[word] == 1:
                wordsCount += 1

        return wordsCount
