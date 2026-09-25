class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        words = []

        prevSpace = 0
        for space in spaces:
            words.append(s[prevSpace:space])
            prevSpace = space

        words.append(s[prevSpace:])

        return " ".join(words)
