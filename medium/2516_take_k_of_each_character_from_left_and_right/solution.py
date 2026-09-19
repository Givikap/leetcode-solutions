class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        charsCounter = [0] * 3
        for c in s:
            charsCounter[ord(c) - 97] += 1

        if any(charsCounter[i] < k for i in range(3)):
            return -1

        window = [0] * 3
        maxWindowLen = 0

        left = 0
        for right in range(len(s)):
            window[ord(s[right]) - 97] += 1

            while left <= right and any(
                charsCounter[i] - window[i] < k for i in range(3)
            ):
                window[ord(s[left]) - 97] -= 1
                left += 1

            maxWindowLen = max(maxWindowLen, right - left + 1)

        return len(s) - maxWindowLen
