class Solution:
    def reverseString(self, s: list[str]) -> None:
        for left, right in zip(
            range(len(s) // 2), range(len(s) - 1, (len(s) - 1) // 2, -1)
        ):
            s[left], s[right] = s[right], s[left]
