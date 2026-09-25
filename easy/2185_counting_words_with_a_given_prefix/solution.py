class Solution:
    def prefixCount(self, words: list[str], prefix: str) -> int:
        return sum(1 for word in words if word.startswith(prefix))
