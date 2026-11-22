class Solution:
    def checkString(self, s: str) -> bool:
        seenB = False

        for c in s:
            if c == "a":
                if seenB:
                    return False
            else:
                seenB = True

        return True
