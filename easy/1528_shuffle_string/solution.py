class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        shuffled_s = [""] * len(s)

        for i, c in zip(indices, s):
            shuffled_s[i] = c

        return "".join(shuffled_s)
