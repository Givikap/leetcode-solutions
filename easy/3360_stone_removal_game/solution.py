class Solution:
    def canAliceWin(self, n: int) -> bool:
        return (
            (n >= 10 and n < 19)
            or (n >= 27 and n < 34)
            or (n >= 40 and n < 45)
            or (n >= 49 and n < 52)
            or (n >= 53 and n < 55)
        )
