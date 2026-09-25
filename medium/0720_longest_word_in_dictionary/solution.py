class Solution:
    def longestWord(self, words: list[str]) -> str:
        words_set = set(words)
        longest_word = ""

        for word in words:
            if (
                len(word) < len(longest_word)
                or len(word) == len(longest_word)
                and word > longest_word
            ):
                continue

            if not {
                word[:prefix_end] for prefix_end in range(1, len(word))
            }.issubset(words_set):
                continue

            longest_word = word

        return longest_word
