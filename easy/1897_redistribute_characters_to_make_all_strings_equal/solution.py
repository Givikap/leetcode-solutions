from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        words_len = len(words)

        for count in Counter("".join(words)).values():
            if count % words_len != 0:
                return False

        return True
