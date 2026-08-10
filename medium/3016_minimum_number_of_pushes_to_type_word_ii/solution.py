class Solution:
    def minimumPushes(self, word: str) -> int:
        charsCounter = [0] * 26
        for ch in word:
            charsCounter[ord(ch) - 97] += 1

        pushesCount = 0
        keysCount = 0

        for count in sorted(charsCounter, reverse=True):
            pushesCount += (keysCount // 8 + 1) * count
            keysCount += 1

        return pushesCount
