from typing import Counter


class Solution:
    def shortestCompletingWord(
        self, licensePlate: str, words: list[str]
    ) -> str:
        licensePlateCounter = Counter(
            c.lower() for c in licensePlate if c.isalpha()
        )

        words.sort(key=lambda word: len(word))

        for word in words:
            for c, count in licensePlateCounter.items():
                if word.count(c) < count:
                    break
            else:
                return word

        return ""
