class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common_chars = []

        for c in set(words[0]):
            common_chars.extend([c] * min(word.count(c) for word in words))

        return common_chars
