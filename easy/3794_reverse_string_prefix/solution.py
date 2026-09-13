class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return "".join(reversed(s[:k])) + s[k:]
