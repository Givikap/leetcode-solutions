class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))

        single_row_words = []

        for word in words:
            for row in rows:
                if all(c.lower() in row for c in word):
                    single_row_words.append(word)

        return single_row_words
