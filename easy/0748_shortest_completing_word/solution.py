from typing import Counter


class Solution:
    def shortestCompletingWord(
        self, licensePlate: str, words: list[str]
    ) -> str:
        licensePlateCounter = Counter(
            c.lower() for c in licensePlate if c.isalpha()
        )

        words.sort(key=lambda word: len(word))
        wordsCounters = [Counter(word) for word in words]

        for i, wordCounter in enumerate(wordsCounters):
            if licensePlateCounter <= wordCounter:
                return words[i]

        return ""
