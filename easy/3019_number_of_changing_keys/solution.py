class Solution:
    def countKeyChanges(self, s: str) -> int:
        keyChanges = 0

        for i in range(len(s) - 1):
            if s[i].lower() != s[i + 1].lower():
                keyChanges += 1

        return keyChanges
