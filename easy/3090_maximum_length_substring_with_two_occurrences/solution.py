class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        charsCounter = [0] * 26

        maxLen = 1

        left = 0
        right = 0

        while right < len(s):
            idx = ord(s[right]) - 97
            charsCounter[idx] += 1

            while charsCounter[idx] > 2:
                charsCounter[ord(s[left]) - 97] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
