class Solution:
    def stringShift(self, s: str, shift: list[list[int]]) -> str:
        s_len = len(s)

        start = 0

        for direction, amount in shift:
            if direction == 0:
                start += amount
            else:
                start -= amount

        return "".join([s[i % s_len] for i in range(start, start + s_len)])
