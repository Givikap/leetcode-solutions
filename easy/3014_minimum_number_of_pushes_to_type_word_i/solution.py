class Solution:
    def minimumPushes(self, word: str) -> int:
        keypadsMap = {}

        pushesCount = 0

        for ch in word:
            keypadsMap[ch] = keypadsMap.get(ch, len(keypadsMap) // 8 + 1)
            pushesCount += keypadsMap[ch]

        return pushesCount
