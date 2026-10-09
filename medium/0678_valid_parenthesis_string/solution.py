class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount = 0
        closeCount = 0

        for left, right in zip(range(len(s)), range(len(s) - 1, -1, -1)):
            if s[left] in ("(", "*"):
                openCount += 1
            else:
                openCount -= 1

            if s[right] in (")", "*"):
                closeCount += 1
            else:
                closeCount -= 1

            if openCount < 0 or closeCount < 0:
                return False

        return True
