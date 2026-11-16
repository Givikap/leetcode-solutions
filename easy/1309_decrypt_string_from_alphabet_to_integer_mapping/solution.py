class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(27, 0, -1):
            s = s.replace(str(i) + ("#" if i > 9 else ""), chr(96 + i))

        return s
